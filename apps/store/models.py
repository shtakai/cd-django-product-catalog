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
