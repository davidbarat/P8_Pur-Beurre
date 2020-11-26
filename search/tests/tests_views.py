from django.test import RequestFactory, TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User

from search.views import searching, register
from search.models import Product, Category, DetailProduct, Substitute
from .tests_models import ModelTest

# Create your tests here.
class ViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = RequestFactory()
        cls.user = User.objects.create_user(
        email='test3@test.te',
        password='test123',
        first_name='Test',
        last_name='test',
        username='Tester'
        )

        cls.category_name = 'Snack'
        Category.objects.create(category_name=cls.category_name)
        # cat.save()
        cls.category = Category.objects.get(id=3)
        Product.objects.create(
            category = cls.category,
            product_id = '1',
            barcode = '00000001',
            product_name = 'test',
            resume = 'test',
            picture_path = 'na',
            small_picture_path = 'na',
            nutriscore_grade = 'na',
            url = 'na'
            )

        cls.product = Product.objects.get(product_id=1)
        DetailProduct.objects.create(
            id = cls.product,
            energy_100g = '100',
            energy_unit = 'kg',
            sugars_100g = '21',
            fiber_100g = '3',
            salt_100g = '2',
            proteins_100g = '20',
            fat_100g = '1',
            saturated_fat_100g = '34',
            carbohydrates_100g = '21'
        )

        cls.client = Client()
        
    def test_searching(self):
        request = self.factory.get('/search/')
        request.user = self.user
        response = searching(request)
        self.assertEqual(response.status_code, 200)
    
    def test_login2(self):
        response = self.client.login(username='test3@test.te', password='test123')
        self.assertEqual(response, True)

    def test_register(self):
        request = self.factory.get('/search/')
        request.user = self.user
        response = register(request)
        self.assertEqual(response.status_code, 200)

    def test_mentions(self):
        url = self.client.get(reverse('mentions'))
        self.assertEqual(url.status_code, 200)

    def test_detail(self):
        self.client.login(username='test3@test.te', password='test123')
        url = self.client.get(
            reverse('detail', args=['1']))
        self.assertEqual(url.status_code, 200)

    def test_save(self):
        self.client.login(username='test3@test.te', password='test123')
        url = self.client.get(
            reverse('save', args=['1']))
        self.assertEqual(url.status_code, 200)
        product = Product.objects.get(product_id=1)
        substitute = Substitute.objects.create(
            user_email='test3@test.te',
            substitute_id=product)
        self.assertEqual(substitute.user_email, 'test3@test.te')



