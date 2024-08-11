from django import forms
from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=250, label="Nombre")
    description = forms.CharField(max_length=500, label="Descripción")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    avaible = forms.BooleanField(initial=True, label="Disponible", required=False)
    photo = forms.ImageField(label="Foto", required=False)

    def save(self):
        Product.objects.create(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            avaible=self.cleaned_data["avaible"],
            photo=self.cleaned_data["photo"],
        )
