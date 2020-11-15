from django.test import TestCase
from django.urls import reverse


class IndexPageTestCase(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_detail_page(self):
        response = self.client.get(reverse('detail'))
        self.assertEqual(response.status_code, 200)
"""
    def test_whatever_list_view(self):
        w = self.create_whatever()
        url = reverse("whatever.views.whatever")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
"""