# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-22 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_about_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='text',
            field=models.TextField(max_length=20000, verbose_name='\u0442\u0435\u043a\u0441\u0442'),
        ),
    ]
