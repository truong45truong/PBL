from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'product',views.Productviewset)
router.register(r'price',views.Priceviewset)
router.register(r'size',views.Sizeviewset)
urlpatterns = [
    path('', include((router.urls))),
]