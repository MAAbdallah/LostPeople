# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2019-06-09 14:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LostPeople', '0002_users_phone_founder'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Missed',
        ),
    ]
