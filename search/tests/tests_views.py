from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth.models import User

from search.views import searching


# Create your tests here.
class ViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
        username='test', email='test@test.te', password='test123')

    def test_searching(self):
        request = self.factory.get('/search/')
        request.user = self.user
        response = searching(request)
        self.assertEqual(response.status_code, 200)
    
    def test_login2(self):
        request = self.factory.get('/search/')
