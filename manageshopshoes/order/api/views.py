from rest_framework import viewsets
from order.models import Orders,Detail_orders 
from .serializers import OrderSerializer,DetailOrderSerializer

class OrderViewset(viewsets.ModelViewSet):
    queryset =  Orders.objects.all()
    serializer_class = OrderSerializer

class DetailOrderViewset(viewsets.ModelViewSet):
    queryset = Detail_orders.objects.all()
    serializer_class = DetailOrderSerializer