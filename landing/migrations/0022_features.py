# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-24 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0021_auto_20190424_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='images/features', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('header_text', models.TextField(max_length=200, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
            ],
            options={
                'verbose_name': '\u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442',
                'verbose_name_plural': '\u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u044b',
            },
        ),
    ]
