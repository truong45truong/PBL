from django.shortcuts import render,redirect
from login.models import User,Customer,Store
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from product.filters import ProductFilter
def homePage(request):
    if (request.user.is_anonymous == False):
        return render(request,'home.html',{ 'current' :request.user })
    else :
        return render(request,'home.html',{ 'current' : False })
# Create your views here.
@login_required
def myAccountPage(request):
    dataCustomerCurrent = Customer.objects.filter(users__username=request.user)
    dataUserCurrent = User.objects.get(username=request.user)
    return render(request,'account.html',{ 'current' :request.user ,
                                           'dataUserCurrent':dataUserCurrent,
                                           'dataCustomerCurrent':dataCustomerCurrent[0]
                                           })
@login_required
def myStorePage(request):
    dataStore = Store.objects.filter(users__username=request.user)
    print(len(dataStore))
    list_product = Product.objects.filter(
        prices__isnull=False, photo_products__isnull=False).values(
        'name', 'slug', 'sex', 'prices__price', 'prices__sale', 'photo_products__name', 'prices__price_total', 'category_id__logo')
    filtered_qs = ProductFilter(request.GET, queryset=list_product).qs
    paginator = Paginator(filtered_qs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.POST : 
        nameUpdate = request.POST.get('')
    if(len(dataStore)==0):
        return redirect('registerstore')
    else:
        return render(request,'store.html',{'page_obj': page_obj, 'pages': range(1, page_obj.paginator.num_pages) ,'dataStore':dataStore[0] ,'current' : request.user })
