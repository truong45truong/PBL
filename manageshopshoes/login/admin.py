from django.contrib import admin
from .models import Users,Stores,Customers,Feedbacks
# Register your models here.

admin.site.register(Users)
admin.site.register(Customers)
admin.site.register(Stores)
admin.site.register(Feedbacks)