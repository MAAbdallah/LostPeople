# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2019-06-19 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Store_Name',
            field=models.CharField(default='storeName', max_length=100),
        ),
    ]
