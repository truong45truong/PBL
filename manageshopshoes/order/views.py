from itertools import product
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Orders, Payments, Detail_orders
from product.models import Products, Photo_products
from login.models import Customers, Users, Stores
from django.contrib.auth.hashers import check_password
from django.shortcuts import HttpResponse
from django.template.defaultfilters import slugify
import json
import datetime
import random
import string
# Create your views here.


def shoppingCartPage(request):

    def handleDuplicateProducts(data):
        dir = dict()
        for item in data:
            if item['slug'] in dir.keys():
                dir[item['slug']] = int(
                    dir[item['slug']]) + int(item['quantity'])
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
            total_price = total_price + \
                int(data[i])*float(item[0]['prices__price_total'])
        return total_price, list_product

    @login_required
    def getProductOfUser(request, data):
        current_user = request.user
        if current_user.is_authenticated:
            user = Users.objects.get(username=current_user)
            customer = Customers.objects.filter(users__username=user)
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
    getProductOfUser(request, data)
    dir_product_cart = handleDuplicateProducts(data)
    total_price, products = processingSynthesisProduct(dir_product_cart)
    return render(request, 'shoppingcart.html', {'product': products, 'total_price': total_price})


def add_to_cart(request):

    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    data = json.loads(request.body.decode('utf-8'))
    product = Products.objects.get(slug=data['slug'])

    def add_with_account(request):
        user = Users.objects.get(username=request.user)
        customer = user.customer_id
        order = Orders(
            name=slugify(""+customer.name+data['slug']+id_generator()),
            datetime=datetime.datetime.now(),
            receiver=customer.name,
            address_receiver=customer.address,
            phone_receiver=user.phone,
            status=False,
            customer_id=customer
        )
        order.save()
        for size in data['sizes']:
            detail_order = Detail_orders(
                status=False, quantity=size['quantity'], product_id=product, order_id=order)
            detail_order.save()

        order.save()

    def add_with_session(request):
        try:
            data_cart = request.session['cart']
        except:
            data_cart = []
        for size in data['sizes']:
            item_cart = {
                'slug' : data['slug'],
                'size' : size['size'],
                'quantity' : size['quantity'] 
            }
            data_cart.append(item_cart)
        request.session['cart'] = data_cart
        print(data_cart)
    if request.user.is_authenticated:
        add_with_account(request)
    else:
        add_with_session(request)
    return HttpResponse(str(data))
