# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, HttpResponse
from models import Slide, Contact, Options, About, Partners, Features, Phone
from django.middleware.csrf import get_token
import requests

# Create your views here.
def send_message(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            e_mail = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['text']

            bot_token = '768364819:AAHyomyBg_2vf7ll1de2FtNHSJrZdcuvL0E'
            bot_chatID = '1001403044490'
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=-' + bot_chatID + \
                        '&parse_mode=Markdown&text=' + u'Имя: ' + name + "\n" + u'Номер телефона: ' + phone + '\n' + \
                        'e-mail: ' + e_mail + "\n" + u'Текст сообщения: ' + message
            """https://api.telegram.org/bot768364819:AAHyomyBg_2vf7ll1de2FtNHSJrZdcuvL0E/sendMessage?chat_id=349390064&parse_mode=Markdown&text=TEST"""

            response = requests.get(send_text)

            return HttpResponse("Спасибо! Ваше сообщение отправлено.")
        except BaseException:
            return HttpResponse("Что-то пошло не так :-(")


phone_number=Phone.objects.last()
options_list=Options.objects.all().order_by('id')

def home_view(request):
    slides_list=Slide.objects.all()
    partners_list=Partners.objects.all()
    features_list=Features.objects.all()
    page_url = request.path
    context = {'slides': slides_list, 'options': options_list, 'page': page_url, \
                              "partners":partners_list, "title": "IT компания", "phone": phone_number,\
                              "features": features_list}
    return render(request, 'home.html', context)

def about_view(request):
    abouts=About.objects.all().order_by('id')
    page_url = request.path
    context = {'abouts': abouts, 'page': page_url, "title": "О компании", "phone": phone_number}
    return render(request, 'about.html', context)

def contacts_view(request):
    contact = Contact.objects.last()
    page_url= request.path
    token=get_token(request)
    context = {'token': token, 'contact': contact, 'page': page_url, "title": "Контакты", "phone": phone_number}
    return render(request, 'contacts.html', context)

def options_view(request, option_slug):
    option = get_object_or_404(Options, slug=option_slug)
    return render(request, 'options.html', {'option': option, 'options': options_list, "phone": phone_number})

def features_view(request, feature_slug):
    feature = get_object_or_404(Features, slug=feature_slug)
    return render(request, 'features.html', {'feature': feature, "phone": phone_number})

def slides_view(request, slide_slug):
    slide = get_object_or_404(Slide, slug=slide_slug)
    return render(request, 'slides.html', {'slide': slide, 'phone': phone_number})

def undr_const(request):
    return render(request, 'under_const.html')