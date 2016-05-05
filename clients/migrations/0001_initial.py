# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-03 18:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nombre')),
                ('phone', models.IntegerField(unique=True, verbose_name='teléfono')),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('address', models.CharField(max_length=255, verbose_name='dirección')),
                ('user', models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
