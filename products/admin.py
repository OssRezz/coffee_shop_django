from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["name", "price", "avaible", "photo"]
    search_fields = ["name", "price"]


admin.site.register(Product, ProductAdmin)
