# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 12:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cmdbinfo',
            old_name='host_name',
            new_name='hostname',
        ),
        migrations.RenameField(
            model_name='cmdbinfo',
            old_name='ip_addr',
            new_name='ip',
        ),
    ]
