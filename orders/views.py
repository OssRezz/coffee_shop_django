from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import DetailView
from .models import Order, OrderProduct
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import JsonResponse
import json

# Create your views here.


class OrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_orders.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user)


def CreateOrder(request):
    if request.method == "POST":
        try:
            # Obtener y parsear el cuerpo de la solicitud como JSON
            data = json.loads(request.body)

            # Obtener el número de la mesa
            table_number = data.get("table_number")

            if not table_number:
                return JsonResponse(
                    {"status": "failed", "message": "Table number is required"},
                    status=400,
                )

            # Obtener el usuario (asegúrate de que el usuario esté autenticado)
            user = request.user

            # Crear la orden
            order = Order.objects.create(user=user, table_number=table_number)

            # Obtener los productos y cantidades
            products = data.get("products", [])

            if not products:
                return JsonResponse(
                    {"status": "failed", "message": "No products provided"}, status=400
                )

            for product_data in products:
                product_id = product_data.get("product")
                quantity = product_data.get("quantity")

                if not product_id or quantity is None:
                    return JsonResponse(
                        {
                            "status": "failed",
                            "message": "Product ID and quantity are required",
                        },
                        status=400,
                    )

                # Crear la relación OrderProduct
                OrderProduct.objects.create(
                    order=order, product_id=product_id, quantity=quantity
                )

            return JsonResponse({"status": "success", "order_id": order.id})

        except json.JSONDecodeError:
            return JsonResponse(
                {"status": "failed", "message": "Invalid JSON"}, status=400
            )

    return JsonResponse(
        {"status": "failed", "message": "Invalid request method"}, status=405
    )
