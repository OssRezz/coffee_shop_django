from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Product


class ProductListViewTest(TestCase):
    def setUp(self):
        # Crear un usuario
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_should_return_200(self):
        # Autenticar al usuario
        self.client.login(username="testuser", password="testpassword")

        # Hacer la solicitud
        url = reverse("list_product")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["products"]().count(), 0)

    def test_should_return_200_with_products(self):
        # Autenticar al usuario
        self.client.login(username="testuser", password="testpassword")
        Product.objects.create(
            name="Latte", description="Cafe y leche", price="5500", avaible=True
        )
        # Hacer la solicitud
        url = reverse("list_product")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["products"]().count(), 1)
