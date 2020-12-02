from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from search.models import Product, Category
from .tests_models import ModelTest


class UrlsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        category_name = "Boissons"
        Category.objects.create(category_name=category_name)
        # cat.save()
        category = Category.objects.get(id=2)
        Product.objects.create(
            category=category,
            product_id="00000002",
            barcode="00000002",
            product_name="test",
            resume="test",
            picture_path="na",
            small_picture_path="na",
            nutriscore_grade="na",
            url="na",
        )

        user = User.objects.create(
            email="test2@test.te",
            password="test123",
            first_name="Test2",
            last_name="test",
            username="Tester2",
        )
        user.save()

        client = Client()

    def test_index_page(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_detail_page(self):
        url = self.client.get(reverse("detail", args=["00000002"]))
        # response = self.client.get(url)
        # self.assertEqual(url, '/search/myproducts/00000001/')
        self.assertEqual(url.status_code, 302)

    def test_save_page(self):

        url = self.client.get(reverse("save", args=["00000002"]))
        # response = self.client.get(url)
        # self.assertEqual(url, '/search/myproducts/00000001/')
        self.assertEqual(url.status_code, 302)

    def test_save_page_authentificated(self):

        self.client.login(username="test2@test.te", password="test123")
        # url = self.client.get(reverse('save', args=['00000001']))
        response = self.client.get(reverse("save", args=["00000002"]))
        # self.assertEqual(str(response.context['username']), 'Tester2')

        # self.assertEqual(url.status_code, 200)

        # Check our user is logged in

        # response = self.client.get(reverse('chistera:dashboard'))

        self.client.logout()
