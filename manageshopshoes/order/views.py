from django.shortcuts import render
from .models import Orders,Payments
from product.models import Products,Photo_products
from django.contrib.sessions.models import Session
import json
# Create your views here.

def shoppingCartPage(request):
    if request.method == 'POST':
        del request.session['cart']
        list_product_cart = json.loads(request.POST.get('cart'))
        request.session['cart']= list_product_cart
    try:
        request.COOKIES['sessionid']
        session = Session.objects.get(session_key=request.COOKIES['sessionid'])
        data = session.get_decoded()
        dir_product_cart = dict()
        for item in data['cart'][:]:
            if item['slug'] in dir_product_cart.keys():
                dir_product_cart[item['slug']] = int(dir_product_cart[item['slug']])+int(item['quantity'])
            else:
                dir_product_cart[item['slug']]=item['quantity']
        dir_product = []
        for i in dir_product_cart.keys():
            dir_product.append(
                {
                    'product': json.dumps(list(Products.objects.filter(
                    prices__isnull=False, photo_products__isnull=False,slug=i).values(
                    'name', 'slug', 'sex', 'prices__price', 'prices__sale', 'photo_products__name', 'prices__price_total', 'category_id__logo'))),
                    'quantity' : dir_product_cart[i]
                }
            )
        
    except Exception as e:
        print(e)
    return render(request,'shoppingcart.html',{'product':dir_product})