from django.urls import path
from . import views

urlpatterns = [
    path('product/',views.getAllProduct),
    path('product/<str>:<slug>/',views.getProduct),
    path('shoppingcart/product',views.getAllProduct)
]
