from dataclasses import fields
from django.db import models
from login.models import Stores,Users
# Create your models here.

class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    slug = models.CharField(null=False,max_length=50)
    name=models.CharField(max_length=50)
    logo=models.ImageField(null=True)
    path=models.TextField(null=True)

    def __str__(self):
        return self.name
class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    slug = models.CharField(null=False,max_length=50)
    name=models.CharField(max_length=50,null=False)
    sex = models.IntegerField(null=True)
    description=models.TextField(null=True)
    store_id=models.ForeignKey(Stores, on_delete=models.SET_NULL, null=True)
    category_id=models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
        
class Sizes(models.Model):
    id = models.BigAutoField(primary_key=True)
    size= models.IntegerField()
    quantity = models.IntegerField(null=True)
    product_id = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True,blank=True,related_name='sizes')

    def __str__(self):
        return self.product_id.name +"-"+ str(self.size)

class Evaluates(models.Model):
    id = models.BigAutoField(primary_key=True)
    rate=models.FloatField()
    description=models.TextField(null=True)
    user_id=models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)

class Prices(models.Model):
    id = models.BigAutoField(primary_key=True)
    price=models.FloatField(null=True)
    sale=models.FloatField(null=True)
    status=models.BooleanField(null=True)
    datetime_create=models.DateTimeField(null=True)
    price_total=models.FloatField(null=True)
    product_id = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True,blank=True,related_name='prices')



class Photo_products(models.Model):
    id = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50,null=True)
    data=models.ImageField()
    product_id = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True,blank=True,related_name='photo_products')

    fields = ['data']
