from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from search.models import Product, Category


class UrlsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        category_name = 'Snack'
        Category.objects.create(category_name=category_name)
        # cat.save()
        category = Category.objects.get(id=1)
        Product.objects.create(
            category = category,
            product_id = '00000001',
            barcode = '00000001',
            product_name = 'test',
            resume = 'test',
            picture_path = 'na',
            small_picture_path = 'na',
            nutriscore_grade = 'na',
            url = 'na'
            )

        user = User.objects.create(
            email =  'test@test.te',
            password = 'test123',
            first_name = 'Test',
            last_name = 'test',
            username  = 'Tester'
            )
        user.save()

        client = Client()

        """
    def setUp(self):

         category_name = 'Snack'
        self.user = User.objects.create_user(
            email='test@test.te',
            password='test123',
            first_name = 'Test',
            last_name = 'test',
            username  = 'Tester')
        self.user.save()

        self.category = Category.objects.create(category_name=category_name)
        self.category.save()
        # category = Category.objects.get(id=1)
        self.product = Product.objects.create(
            category = category,
            product_id = '00000001',
            barcode = '00000001',
            product_name = 'test',
            resume = 'test',
            picture_path = 'na',
            small_picture_path = 'na',
            nutriscore_grade = 'na',
            url = 'na'
            )"""
        

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_detail_page(self):
        url = self.client.get(
            reverse('detail', args=['00000001']))
        # response = self.client.get(url)
        # self.assertEqual(url, '/search/myproducts/00000001/')
        self.assertEqual(url.status_code, 302)

    def test_save_page(self):

        url = self.client.get(
            reverse('save', args=['00000001']))
        # response = self.client.get(url)
        # self.assertEqual(url, '/search/myproducts/00000001/')
        self.assertEqual(url.status_code, 302)

    def test_save_page_authentificated(self):

        self.client.login(username='test@test.te', password='test123')
        # url = self.client.get(reverse('save', args=['00000001']))
        response = self.client.get(reverse('save', args=['00000001']))
        self.assertEqual(str(response.context['user']), 'Tester')

        # self.assertEqual(url.status_code, 200)
        
        
        # Check our user is logged in

        # response = self.client.get(reverse('chistera:dashboard'))
        
        self.client.logout()