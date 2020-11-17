from django.test import TestCase
from search.forms import RegisterForm, UserForm
# Create your tests here.


class FormTest(TestCase):

    @classmethod
    def setUpTestData(self):

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

        self.form = UserForm(data=self.dataUserForm)
        self.assertTrue(self.form.is_valid())

"""
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data
"""