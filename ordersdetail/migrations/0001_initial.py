# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-03 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordersdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='cantidad')),
                ('subtotal_price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='subtotal')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='pedido')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='producto')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]