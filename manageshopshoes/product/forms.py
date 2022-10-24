from dataclasses import fields
from secrets import choice
from django.forms import ModelForm
from .models import Products,Photo_products,Prices,Sizes
from django import forms

class ProductForm(ModelForm):
    CHOICE=(
        ("0","All"),
        ("1","Men"),
        ("2","Women")
    )
    gender = forms.ChoiceField(choices=CHOICE)
    class Meta:
        model = Products
        fields = ['name','gender','category_id','description']
class PhotoProductForm(ModelForm):
    class Meta:
        model =Photo_products
        fields =['data']
class PriceForm(ModelForm):
    class Meta:
        model = Prices
        fields = ['price','sale']