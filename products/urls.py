# from django.contrib import admin
from django.urls import path
from .views import ProductListView, ProductFormView

urlpatterns = [
    path("add/", ProductFormView.as_view(), name="add_product"),
    path("list/", ProductListView.as_view()),
]
