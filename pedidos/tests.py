from django.test import TestCase
from django.urls import reverse

class HomeViewTests(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get(reverse('pedidos:home'))
        self.assertEqual(response.status_code, 200)
