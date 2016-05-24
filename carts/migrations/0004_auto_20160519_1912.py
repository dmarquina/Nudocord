# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-20 00:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_remove_cart_ipaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='producto'),
        ),
    ]
