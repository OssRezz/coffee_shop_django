from django.views import generic
from django.views.generic.base import TemplateView
from .forms import ProductForm
from django.urls import reverse_lazy
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from .serializers import PuductSerializer
from rest_framework.response import Response


class ProductFormView(LoginRequiredMixin, generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("list_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListView(LoginRequiredMixin, TemplateView):
    template_name = "products/list.html"

    def get_context_data(self):

        product_list = Product.objects.all

        return {"products": product_list}


class ProductListApi(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        products = Product.objects.all()
        serializer = PuductSerializer(products, many=True)

        return Response(serializer.data)
