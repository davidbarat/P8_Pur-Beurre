from django.test import TestCase
from django.urls import reverse


class PageTestCase(TestCase):

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
        