from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('<slug:slug>',views.productPage,name='product'),
    path('<slug:slug>/<slug:slugproduct>/',views.productDetail,name='productdetail'),
    path('<slug:slugstore>/productnew',views.productNewPage,name='productnew'),
]