# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from models import Slide, Contact, Options, About, Partners, Phone, Features
import requests

# Create your views here.
def send_message(request):
    name = request.POST['name']
    e_mail = request.POST['email']
    message = request.POST['text']
    bot_message = {
        "Имя: ": name,
        "e-mail: ": e_mail,
        "Текст сообщения: ": message
    }

    bot_token = '768364819:AAHyomyBg_2vf7ll1de2FtNHSJrZdcuvL0E'
    bot_chatID = '349390064'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=-' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    """https://api.telegram.org/bot768364819:AAHyomyBg_2vf7ll1de2FtNHSJrZdcuvL0E/sendMessage?chat_id=349390064&parse_mode=Markdown&text=TEST"""

    response = requests.get(send_text)

    return response.json()

def home_view(request):
    slides_list=Slide.objects.all()
    options_list=Options.objects.all()
    partners_list=Partners.objects.all()
    phone_number=Phone.objects.last()
    features_list=Features.objects.all()
    page_url = request.path
    context = {'slides': slides_list, 'options': options_list, 'page': page_url, \
                              "partners":partners_list, "title": "IT компания", "phone": phone_number,\
                              "features": features_list}
    return render(request, 'home.html', context)

def about_view(request):
    abouts=About.objects.all().order_by('id')
    page_url = request.path
    context = {'abouts': abouts, 'page': page_url, "title": "О компании"}
    return render(request, 'about.html', context)

def contacts_view(request):
    contact = Contact.objects.last()
    page_url= request.path
    context = {'contact': contact, 'page': page_url, "title": "Контакты"}
    return render(request, 'contacts.html', context)