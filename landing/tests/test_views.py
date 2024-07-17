from django.urls import reverse
from django.test import TestCase

class TestLanding(TestCase):
    """ landing page test """
    def test_get_landing_page(self):
        url = reverse("/")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing/landing.html")