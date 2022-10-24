from django.shortcuts import render
from .models import Orders,Payments
from product.models import Products,Photo_products
# Create your views here.

def shoppingCartPage(request):
    return render(request,'shoppingcart.html')