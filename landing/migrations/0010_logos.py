# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-22 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0009_auto_20190422_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='images/logos', verbose_name='\u043b\u043e\u0433\u043e')),
            ],
        ),
    ]
