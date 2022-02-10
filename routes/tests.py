from django.test import TestCase
from django.test import Client


class RoutesTestCase(TestCase):
    client = None

    def setUp(self):
        self.client = Client()

    def test_index_path(self):
        response = self.client.get('/routes/')
        self.assertEqual(200, response.status_code)

    def test_search_path(self):
        response = self.client.get('/routes/search/MYR/ATL/')
        self.assertEqual(200, response.status_code)
