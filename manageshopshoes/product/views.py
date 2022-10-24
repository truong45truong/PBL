from django.shortcuts import render,redirect
from .forms import ProductForm,PriceForm,PhotoProductForm
from .models import Categories, Photo_products, Products , Prices,Sizes
from django.core.paginator import Paginator
from .filters import ProductFilter
from slugify import slugify
import os
import shutil
import datetime
import random
import string
# path save photo

path_upload = "C:/Users/DELL/OneDrive/Máy tính/8-2022/djangotrain/PBL/manageshopshoes/media_upload/photos"
path_root = "C:/Users/DELL/OneDrive/Máy tính/8-2022/djangotrain/PBL/manageshopshoes/media/photos"
# Create your views here.

def productPage(request,slug):
    sex=request.GET.get('sexselect')
    category = request.GET.get('categoryselect')
    limit = request.GET.get('limitselect')
    sort_price = request.GET.get('sortselect')
    topsale = request.GET.get('topsale')
    latest = request.GET.get('latest')
    price = request.POST.get('task')
    print(price)
    list_product =  Products.objects.filter(
                    prices__isnull=False,photo_products__isnull=False,category_id__slug=slug).values(
                    'name','slug','sex','prices__price','prices__sale','photo_products__name','prices__price_total','category_id__logo')
    if topsale:
        pass
    if latest:
        pass
    if sex:
        list_product =list_product.filter(sex=sex)
        filtered_qs = ProductFilter(request.GET,queryset=list_product).qs
    if limit:
        list_limit=str(limit).split("-")
        try:
            low=int(list_limit[0])
        except:
            low=0
        try:
            hight=int(list_limit[1])
        except:
            hight=0
        if low != 0:
            list_product =list_product.filter(prices__price_total__gte=low)
        if hight != 0:
            list_product =list_product.filter(prices__price_total__lte=hight)
        filtered_qs = ProductFilter(request.GET,queryset=list_product).qs
    if category:
        category =list_product.filter(category_id__id=category)
    if sort_price:
        if sort_price == "low":
            list_product =list_product.order_by('prices__price_total')
        if sort_price == "hight":
            list_product =list_product.order_by('-prices__price_total')
        filtered_qs = ProductFilter(request.GET,queryset=list_product).qs
    if sex is None and category is None and limit is None and sort_price is None:
        filtered_qs = ProductFilter(request.GET,queryset=list_product).qs
    paginator = Paginator(filtered_qs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'products.html' , {'page_obj' : page_obj,'pages':range(1,page_obj.paginator.num_pages)})
def productDetail(request,slug,slugproduct):
    return render(request,'ProductDetail.html')

def productNewPage(request,slugstore):
    
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    form_product = ProductForm()
    form_price = PriceForm()
    form_photoproduct = PhotoProductForm()
    if request.method == 'POST':
        form_product = ProductForm(request.POST)
        form_price = PriceForm(request.POST) 
        form_photoproduct = PhotoProductForm(request.POST,request.FILES) 
        if form_product.is_valid(): 
            name = form_product.cleaned_data['name']
            sex = form_product.cleaned_data['gender']
            description = form_product.cleaned_data['description']
            category = form_product.cleaned_data['category_id']
            while True:
                try:
                    product = Products(name=name,sex=sex,description=description,category_id=category,slug=slugify(name)+"-"+id_generator())
                    break
                except:
                    pass
            product.save()
            for i in range(35,45):
                quantity=request.POST.get('sizevalue_'+str(i))
                print(quantity)
                Sizes(size=i,quantity=quantity,product_id=product).save()
                
        if form_price.is_valid():
            price = form_price.cleaned_data['price']
            sale = form_price.cleaned_data['sale']
            price_product = Prices(price=price,sale=sale,price_total=(100-float(sale))*float(price)/100,product_id=Products(id= product.id),datetime_create=datetime.datetime.now())
            price_product.save()
        if form_photoproduct.is_valid():
            upload(request.FILES['data'],product.id)
            handleImageUpload(request.FILES['data'],product.id)

    return render(request,'productnew.html',{'form_product':form_product,'form_price':form_price,'form_photoproduct':form_photoproduct})
def upload(f,product):
    if(f.name.split('.')[-1] in ['png','jpg','webp']):
        file = open(
                os.path.join(path_upload,"products",str(product)+'.'+f.name.split('.')[-1]),
                'wb+'
                )
        for chunk in f.chunks():
            file.write(chunk)
        file.close()
    # code handle upload

def handleImageUpload(f,product):
    nameFile = str(product) + '.' + f.name.split('.')[-1]
    shutil.move(path_upload + '/products'  + '/' + nameFile, path_root + '/products' + '/' + nameFile)
    photo_product = Photo_products(name=nameFile , data=nameFile ,product_id= Products(id= product) )
    photo_product.save()