# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from models import Slide, Contact, Options, About, Logos
# from django.template import RequestContext

# Create your views here.
def send_mail(request):
    pass

def home_view(request):
    slides_list=Slide.objects.all()
    options_list=Options.objects.all()
    logos_list=Logos.objects.all()
    page_url = request.path
    return render_to_response('home.html', {'slides': slides_list, 'options': options_list, 'page': page_url, \
                                            "logos" :logos_list, "title": "IT компания"})

def about_view(request):
    abouts=About.objects.all().order_by('id')
    page_url = request.path
    return render_to_response('about.html', {'abouts': abouts, 'page': page_url, "title": "О компании"})

def contacts_view(request):
    contact = Contact.objects.last()
    page_url= request.path
    return render_to_response('contacts.html', {'contact': contact, 'page': page_url, "title": "Контакты"})