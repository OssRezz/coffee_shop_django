# # from django.contrib import admin
from django.urls import path
from .views import OrderView

urlpatterns = [
    path("my-orders/", OrderView.as_view(), name="my_orders"),
]
