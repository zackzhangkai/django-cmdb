# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170413_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmdbinfo',
            name='ip',
            field=models.TextField(),
        ),
    ]
