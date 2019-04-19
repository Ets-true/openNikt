# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Slide(models.Model):
    header_text=models.CharField('заголовок', max_length=200)
    description=models.CharField('описание', max_length=200)
    image=models.ImageField(verbose_name='фото', upload_to="images/slides")

    class Meta:
        verbose_name = u'Слайд'
        verbose_name_plural = u'Слайды'

    def __unicode__(self):
        return u'%s' % self.header_text

class Options(models.Model):
    header_text=models.CharField('заголовок', max_length=200)
    text=models.TextField('текст', max_length=200)

    class Meta:
        verbose_name = u'Вид деятельности'
        verbose_name_plural = u'Виды деятельности'

    def __unicode__(self):
        return u'%s' % self.header_text

class Contact(models.Model):
    header_text=models.CharField('заголовок', max_length=200)
    text=models.TextField('текст', max_length=200)

    class Meta:
        verbose_name = u'Контакты'
        verbose_name_plural = u'Контакты'

    def __unicode__(self):
        return u'%s' % self.header_text