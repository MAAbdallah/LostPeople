# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2019-06-11 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LostPeople', '0007_missed_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missed',
            name='age',
            field=models.IntegerField(default=1),
        ),
    ]