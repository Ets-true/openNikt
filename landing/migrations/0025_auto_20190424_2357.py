# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-24 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0024_auto_20190424_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='subheader_text',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u043f\u043e\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
    ]
