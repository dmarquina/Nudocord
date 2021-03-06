# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-13 18:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deliverplaces', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('PR', 'Proceso'), ('EN', 'Entregado'), ('CA', 'Cancelado')], max_length=2, verbose_name='estado')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='precio total')),
                ('registration_date', models.DateField(auto_now_add=True, verbose_name='fecha de registro')),
                ('deliver_date', models.DateField(verbose_name='fecha de entrega')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='cliente')),
                ('deliverplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliverplaces.Deliverplace', verbose_name='lugar de entrega')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Ordersdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='cantidad')),
                ('subtotal_amount', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='subtotal')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='pedido')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='producto')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
