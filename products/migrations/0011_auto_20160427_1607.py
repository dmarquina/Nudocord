# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-27 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20160427_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=255, verbose_name='categoria'),
        ),
    ]
