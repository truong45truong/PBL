from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager

# Create your models here.
class Stores(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.TextField()
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    fax = models.CharField(max_length=50)
    email = models.EmailField()
    logo = models.ImageField(null=True)

class Customers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    birthday = models.DateField()

class Users(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=10)
    avatar = models.ImageField(null=True, default="avatar.svg")
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    store_id = models.ForeignKey(Stores, on_delete=models.SET_NULL, null=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.SET_NULL, null=True)

    objects = UserManager()
    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

class Feedbacks(models.Model):
    id = models.BigAutoField(primary_key=True)
    reason = models.CharField(max_length=200,null=False)
    note = models.TextField(null=True)
    replay = models.TextField(null=True)
    user_id = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
