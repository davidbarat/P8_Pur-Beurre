import re
from django.test import RequestFactory, TestCase, Client
from django.urls import reverse, NoReverseMatch
from django.contrib.auth.models import AnonymousUser, User
from django.core import mail
from django.test.utils import override_settings
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate
from search.views import searching, register
from search.models import Product, Category, DetailProduct, Substitute
from search.forms import RegisterForm, UserForm
from .tests_models import ModelTest

def password_reset_confirm_url(uidb64, token):
        try:
            print(reverse("password_reset_confirm", args=(uidb64, token)))
            return reverse("password_reset_confirm", args=(uidb64, token))
        except NoReverseMatch:
            return f"/accounts/reset/invaliduidb64/invalid-token/"

def utils_extract_reset_tokens(full_url):
    return re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', 
        full_url)

class ViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = RequestFactory()

        cls.data = {
            "email":"test4@test.te",
            "password":"test123",
            "first_name":"Test4",
            "last_name":"test4",
            "username":"Tester4",
        }

        cls.user = User.objects.create_user(
            email="test3@test.te",
            password="test123",
            first_name="Test",
            last_name="test",
            username="Tester",
        )
        cls.user.save()

        cls.category_name = "Snack"
        Category.objects.create(category_name=cls.category_name)
        # cat.save()
        cls.category = Category.objects.get(id=3)
        Product.objects.create(
            category=cls.category,
            product_id="1",
            barcode="00000001",
            product_name="test",
            resume="test",
            picture_path="na",
            small_picture_path="na",
            nutriscore_grade="na",
            url="na",
        )

        cls.product = Product.objects.get(product_id=1)
        DetailProduct.objects.create(
            id=cls.product,
            energy_100g="100",
            energy_unit="kg",
            sugars_100g="21",
            fiber_100g="3",
            salt_100g="2",
            proteins_100g="20",
            fat_100g="1",
            saturated_fat_100g="34",
            carbohydrates_100g="21",
        )

        cls.client = Client()
        
    def test_searching(self):
        request = self.factory.get("/search/")
        request.user = self.user
        response = searching(request)
        self.assertEqual(response.status_code, 200)

    def test_login2(self):
        response = self.client.login(username="test3@test.te", password="test123")
        self.assertEqual(response, True)

    def test_logout2(self):
        url = self.client.get(reverse("index"))
        self.assertEqual(url.status_code, 200)

    def test_register(self):
        request = self.factory.get("/search/")
        request.user = self.user
        response = register(request)
        self.assertEqual(response.status_code, 200)
        self.formUserForm = RegisterForm(data=self.data)
        self.assertTrue(self.formUserForm.is_valid())

    def test_mentions(self):
        url = self.client.get(reverse("mentions"))
        self.assertEqual(url.status_code, 200)

    def test_detail(self):
        self.client.login(username="test3@test.te", password="test123")
        url = self.client.get(reverse("detail", args=["1"]))
        self.assertEqual(url.status_code, 200)

    def test_save(self):
        self.client.login(username="test3@test.te", password="test123")
        url = self.client.get(reverse("save", args=["1"]))
        self.assertEqual(url.status_code, 200)
        product = Product.objects.get(product_id=1)
        substitute = Substitute.objects.create(
            user_email="test3@test.te", substitute_id=product
        )
        self.assertEqual(substitute.user_email, "test3@test.te")

    def test_myproducts(self):
        self.client.login(username="test3@test.te", password="test123")
        url = self.client.get(reverse("myproducts"))
        self.assertEqual(url.status_code, 200)

    def test_update_password(self):
        self.client.login(username="test3@test.te", password="test123")
        self.response = self.client.post('/password/',
            {'old_password': 'test3@test.te',
            'new_password1': 'test456',
            'new_password2': 'test456'
            }
            )
        self.assertEqual(self.response.status_code, 200)

# @override_settings(EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend')
class DefaultEmailTestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.factory = RequestFactory()
        cls.user = User.objects.create_user(
            email="test3@test.te",
            password="test123",
            first_name="Test",
            last_name="test",
            username="Tester",
        )
        cls.user.save()

    def test_password_reset(self):
        self.client.post(
            '/password_reset',
            {"email": "test3@test.te"},
            follow=True)
        
        self.assertEqual(len(mail.outbox), 1)

        msg = mail.outbox[0]
        # print(mail.outbox[0].body)
        url = utils_extract_reset_tokens(msg.body)
        self.extract_url = url[0]
        self.uidb64 = self.extract_url.split('/')[4]
        self.token = self.extract_url.split('/')[5]
        
        self.response = self.client.get(
            password_reset_confirm_url(self.uidb64, self.token), 
            follow=True)
        
        self.assertEqual(self.response.status_code, 200)

        self.response = self.client.post(password_reset_confirm_url(self.uidb64, "set-password"),
                                      {"new_password1": 'test456',
                                       "new_password2": 'test456'},
                                      follow=True)

        self.assertIsNone(authenticate(email='test3@test.te',password='test123'))