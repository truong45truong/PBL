from django.contrib import admin
from .models import Product, Price, Photo_product, Evaluate, Categorie, Size
# Register your models here.
admin.site.register(Price)
admin.site.register(Product)
admin.site.register(Photo_product)
admin.site.register(Evaluate)
admin.site.register(Categorie)
admin.site.register(Size)