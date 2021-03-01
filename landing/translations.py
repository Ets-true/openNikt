# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from models import  Options, Contact, About, Features

class SlideTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Page.
    """
    fields = ('header_text', 'description', 'button_caption', 'material_text', )


class OptionsTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Page.
    """
    fields = ('header_text', 'text', )


class ContactTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Page.
    """
    fields = ('header_text', 'text', 'file', )


class AboutTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Page.
    """
    fields = ('header_text', 'text', )


class FeaturesTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Page.
    """
    fields = ('header_text', 'subheader_text', )


translator.register(Options, OptionsTranslationOptions)
translator.register(Contact, ContactTranslationOptions)
translator.register(About, AboutTranslationOptions)
translator.register(Features, FeaturesTranslationOptions)