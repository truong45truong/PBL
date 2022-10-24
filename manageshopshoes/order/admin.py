from django.contrib import admin
from .models import Transports,Orders,Detail_orders,Payments
# Register your models here.

admin.site.register(Transports)
admin.site.register(Orders)
admin.site.register(Detail_orders)
admin.site.register(Payments)