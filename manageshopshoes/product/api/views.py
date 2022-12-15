from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from product.models import Product, Size, Price
from .serializers import PriceSerializer, ProductSerializer, SizesSerializer

class Productviewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class Priceviewset(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
class Sizeviewset(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizesSerializer
