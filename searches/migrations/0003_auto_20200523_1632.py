# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-23 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searches', '0002_auto_20200523_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(max_length=1060),
        ),
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(max_length=160),
        ),
    ]
