from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class OrderViewTest(TestCase):

    def test_no_logged_user_should_redirect(self):
        url = reverse("my_orders")
        response = self.client.get(url)
        self.assertEqual(response.url, "/?next=/orders/my-orders/")

    def test_logged_user_should_redirect(self):
        url = reverse("my_orders")
        user = get_user_model().objects.create(
            username="testuser", password="testpassword"
        )
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
