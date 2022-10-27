from django.shortcuts import render
from .models import Orders,Payments
from product.models import Products,Photo_products
import json
import requests
# Create your views here.

def shoppingCartPage(request):
    print(request.session)
    list_item_cart= request.session.get('list_shopping_cart')
    repos_info = json.loads(requests.get("http://127.0.0.1:8000/api/product/").text)
    print("danh sach",repos_info)
    return render(request,'shoppingcart.html')