# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 20:58
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
    ]