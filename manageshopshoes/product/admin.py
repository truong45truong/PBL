from django.contrib import admin
from .models import Products,Prices,Photo_products,Evaluates,Categories,Sizes
# Register your models here.
admin.site.register(Prices)
admin.site.register(Products)
admin.site.register(Photo_products)
admin.site.register(Evaluates)
admin.site.register(Categories)
admin.site.register(Sizes)