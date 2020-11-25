from django.test import TestCase
from search.forms import RegisterForm, UserForm

from django.contrib.auth.models import User

# Create your tests here.


class FormTest(TestCase):

    @classmethod
    def setUp(self):

        self.data = {
            'email': 'test@test.te',
            'password': 'test123',
            'first_name': 'Test',
            'last_name': 'test',
            'username': 'Tester'
            }

        self.dataUserForm = {
            'username': 'test@test.te',
            'password': 'test123',
            }

    def test_valid_RegisterForm(self):

        self.form = RegisterForm(data=self.data)
        self.assertTrue(self.form.is_valid())

    def test_valid_UserForm(self):

        self.user = User.objects.create_user(
        username='test', 
        email='test@test.te',
        password='test123',
        last_name='test',
        first_name='Test',
        )
        self.user.save()

        # self.getuser = User.objects.get(id=1)
        self.formUserForm = UserForm(data=self.dataUserForm)
        self.assertTrue(self.formUserForm.is_valid())
