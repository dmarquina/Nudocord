# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-13 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deliverplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='nombre')),
                ('address', models.CharField(max_length=255, verbose_name='direccion')),
                ('date', models.DateField(null=True, verbose_name='fecha')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
