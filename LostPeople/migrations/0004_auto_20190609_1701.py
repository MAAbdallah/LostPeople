# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2019-06-09 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LostPeople', '0003_auto_20190609_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missed',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
