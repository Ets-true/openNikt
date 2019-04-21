from django.shortcuts import render, render_to_response, get_object_or_404
from models import Slide, Contact, Options, About

# Create your views here.
def home_view(request):
    slides_list=Slide.objects.all()
    options_list=Options.objects.all()
    return render_to_response('home.html', {'slides': slides_list, 'options': options_list})

def about_view(request):
    about=About.objects.last()
    return render_to_response('about.html', {'about_text': about})

def send_mail(request):
    pass

def contacts_view(request):
    return render_to_response('contacts.html')