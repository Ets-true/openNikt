# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-22 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0030_auto_20190522_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='material_text',
            field=models.TextField(blank=True, max_length=20000, verbose_name='\u0442\u0435\u043a\u0441\u0442 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b'),
        ),
    ]
