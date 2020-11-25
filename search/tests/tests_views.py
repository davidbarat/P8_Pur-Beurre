from django.test import RequestFactory, TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User

from search.views import searching, register
from search.models import Product, Category
from .tests_models import ModelTest

# Create your tests here.
class ViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
        email='test3@test.te',
        password='test123',
        first_name='Test',
        last_name='test',
        username='Tester'
        )

        self.client = Client()
        
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
        """
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Company Name XYZ') """

    def test_mentions(self):
        url = self.client.get(reverse('mentions'))
        self.assertEqual(url.status_code, 200)

    # def test_detail(self):
