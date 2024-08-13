from rest_framework.serializers import ModelSerializer
from .models import Product


class PuductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "avaible",
            "photo",
        ]
