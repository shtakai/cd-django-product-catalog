from django.contrib import admin
from .models import Manufacturer, Product, Order, Cart

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
