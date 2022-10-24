from django.db import models
from product.models import Products
from login.models import Customers
# Create your models here.

class Transports(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    logo = models.ImageField(null=True)
    price = models.FloatField(null=True)

class Orders(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    datetime = models.DateTimeField()
    receiver = models.CharField(max_length=50,null=True)
    address_receiver = models.CharField(max_length=200,null=True)
    phone_receiver = models.CharField(max_length=10,null=True)
    status = models.BooleanField()
    total_price = models.FloatField(null=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.SET_NULL, null=True)
    transport_id = models.ForeignKey(Transports, on_delete=models.SET_NULL, null=True)

class Payments(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()
    allowed = models.BooleanField()
    datetime = models.DateTimeField()
    order_id = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True)

class Detail_orders(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.BooleanField()
    quantity = models.IntegerField()
    order_id = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)

