from django.db import models
from django.core.validators import MinLengthValidator


class Product(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(8)])
    price = models.FloatField()
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
    shipping_name = models.CharField(max_length=50)
    shipping_address = models.CharField(max_length=255)
    card_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orders'


class Cart(models.Model):
    product = models.ForeignKey('Product')
    order = models.ForeignKey('Order')
    amount = models.PositiveSmallIntegerField(default=0)
    unit_price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'carts'
