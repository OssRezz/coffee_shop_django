from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import DetailView
from .models import Order
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class OrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_orders.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user)
