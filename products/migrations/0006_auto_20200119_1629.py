# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-19 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200119_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productview',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.DeleteModel(
            name='ProductView',
        ),
    ]