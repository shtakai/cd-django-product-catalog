from django.db import models
from django.core.validators import MinLengthValidator


class Product(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(8)])
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updted_at = models.DateTimeField(auto_now_add=True)
    manufacturer = models.ForeignKey('Manufacturer')

    class Meta:
        db_table = 'products'


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'manufacturers'


class Order(models.Model):
    shipping_status = models.BooleanField(default=False)
    shipping_name = models.CharField(max_length=50, null=True)
    shipping_address = models.CharField(max_length=255, null=True)
    card_number = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orders'


class Cart(models.Model):
    product = models.ForeignKey('Product')
    order = models.ForeignKey('Order')
    amount = models.PositiveSmallIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'carts'
