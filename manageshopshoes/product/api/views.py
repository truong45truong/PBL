from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from product.models import Products, Sizes, Prices
from .serializers import PriceSerializer, ProductSerializer, SizesSerializer

class Productviewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
class Priceviewset(viewsets.ModelViewSet):
    queryset = Prices.objects.all()
    serializer_class = PriceSerializer
class Sizeviewset(viewsets.ModelViewSet):
    queryset = Sizes.objects.all()
    serializer_class = SizesSerializer
