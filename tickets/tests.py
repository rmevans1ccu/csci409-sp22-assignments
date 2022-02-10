from django.test import TestCase
from django.test import Client


class TicketsTestCase(TestCase):
    client = None

    def setUp(self):
        self.client = Client()

    def test_index_path(self):
        response = self.client.get('/tickets/')
        self.assertEqual(200, response.status_code)

    def test_search_path(self):
        response = self.client.get('/tickets/1234567890/')
        self.assertEqual(200, response.status_code)
