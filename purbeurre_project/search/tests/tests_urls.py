from django.test import TestCase
from django.urls import reverse


class IndexPageTestCase(TestCase):
coverage run manage.py test
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)