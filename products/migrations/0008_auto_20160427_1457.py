# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-27 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20160427_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('GS', 'Gaucho simple'), ('GS2', 'Gaucho simple de dos colores'), ('GD', 'Gaucho doble'), ('GD3', 'Gaucho doble de tres colores')], max_length=3, verbose_name='categoria'),
        ),
    ]
