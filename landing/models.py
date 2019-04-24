# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Slide(models.Model):
    L = 'left'
    C = 'center'
    R = 'right'

    POSITION_CHOICES = (
        (L, 'Слева'),
        (C, 'По центру'),
        (R, 'Справа')
    )

    header_text=models.CharField('заголовок', max_length=200)
    description=models.CharField('описание', max_length=200)
    button_caption=models.CharField('надпись на кнопке', max_length=200, blank=True)
    image=models.ImageField(verbose_name='фото', upload_to="images/slides")
    text_position=models.CharField('позиция текста', max_length=1, choices=POSITION_CHOICES, default=L)

    class Meta:
        verbose_name = u'Слайд'
        verbose_name_plural = u'Слайды'

    def __unicode__(self):
        return u'%s' % self.header_text

class Options(models.Model):
    image=ImageField(verbose_name='изображение', upload_to="images/options")
    header_text=models.CharField('заголовок', max_length=100)
    text=models.TextField('текст', max_length=2000)

    class Meta:
        verbose_name = u'Вид деятельности'
        verbose_name_plural = u'Виды деятельности'

    def __unicode__(self):
        return u'%s' % self.header_text

class Features(models.Model):
    image=ImageField(verbose_name='изображение', upload_to="images/features")
    header_text=models.CharField('заголовок', max_length=200)
    subheader_text=models.CharField('подзаголовок', max_length=100, blank=True)

    class Meta:
        verbose_name=u'аргумент'
        verbose_name_plural=u'аргументы'

    def __unicode__(self):
        return u'%s' % self.header_text

class Contact(models.Model):
    header_text=models.CharField('заголовок', max_length=200)
    text=models.TextField('текст', max_length=20000)
    file=models.FileField('карточка контрагента', blank=True)

    class Meta:
        verbose_name = u'Контакты'
        verbose_name_plural = u'Контакты'

    def __unicode__(self):
        return u'%s' % self.header_text

class About(models.Model):
    header_text=models.CharField('заголовок', max_length=200)
    text=models.TextField('текст', max_length=20000)
    image=models.ImageField(verbose_name='фото', upload_to="images/about", blank=True)

    def __unicode__(self):
        return u'%s' % self.header_text

class Partners(models.Model):
    title=models.CharField('название', max_length=200)
    is_vendor=models.BooleanField(verbose_name='Вендор?')
    image=ImageField(verbose_name='лого', upload_to="images/logos")
    link=models.CharField('Ссылка на сайт', max_length=200, blank=True)

    class Meta:
        verbose_name = u'Партнер'
        verbose_name_plural = u'Партнеры'

    def __unicode__(self):
        return u'%s' % self.title

class Phone(models.Model):
    number=models.CharField('Номер телефона', max_length=20)

    def __unicode__(self):
        return u'%s' % self.number

    class Meta:
        verbose_name = u'Номер телефона'
        verbose_name_plural = u'Номера телефонов'