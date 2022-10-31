from itertools import product
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Orders, Payments, Detail_orders
from product.models import Products, Photo_products
from login.models import Customers, Users
from django.contrib.auth.hashers import check_password
import json
# Create your views here.


def shoppingCartPage(request):

    def handleDuplicateProducts(data):
        dir = dict()
        for item in data:
            if item['slug'] in dir.keys():
                dir[item['slug']] = int(dir[item['slug']]) + int(item['quantity'])
            else:
                dir[item['slug']] = item['quantity']
        return dir

    def processingSynthesisProduct(data):
        list_product = []
        total_price = 0
        for i in data.keys():
            item = Products.objects.filter(
                prices__isnull=False, photo_products__isnull=False, slug=i).values(
                'name', 'slug', 'sex', 'prices__price', 'prices__sale', 
                'photo_products__name', 'prices__price_total', 'category_id__logo'
            )
            list_product.append(
                {
                    'name': item[0]['name'],
                    'slug': item[0]['slug'],
                    'sex': item[0]['sex'],
                    'sale': item[0]['prices__sale'],
                    'photo': item[0]['photo_products__name'],
                    'price_total': item[0]['prices__price_total'],
                    'category': item[0]['category_id__logo'],
                    'quantity': dir_product_cart[i]
                }
            )
            total_price = total_price + int(data[i])*float(item[0]['prices__price_total'])
        return total_price,list_product

    @login_required
    def getProductOfUser(request,data):
        current_user = request.user
        user = Users.objects.get(login=current_user)
        user = Users.objects.get(login=current_user)
        if check_password(user.password, current_user.password):
            customer = Customers.objects.filter(users__login=current_user)
            product_cart_user = Orders.objects.filter(customer_id=customer[0], detail_orders__isnull=False).values(
                'detail_orders__product_id__slug', 'detail_orders__quantity'
            )
        for item in product_cart_user:
            data.append({
                'slug': item['detail_orders__product_id__slug'],
                'quantity': item['detail_orders__quantity']
            })
    try:
        data = request.session['cart']
    except Exception:
        data = []
    getProductOfUser(request,data)
    dir_product_cart = handleDuplicateProducts(data)
    total_price,products = processingSynthesisProduct(dir_product_cart)

    return render(request, 'shoppingcart.html', {'product': products, 'total_price': total_price})
