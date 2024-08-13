# from django.contrib import admin
from django.urls import path
from .views import ProductListView, ProductFormView, ProductListApi

urlpatterns = [
    path("", ProductListView.as_view(), name="list_product"),
    path("add/", ProductFormView.as_view(), name="add_product"),
    path("api/", ProductListApi.as_view(), name="api_list_products"),
]
