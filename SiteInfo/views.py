from unicodedata import category
from django.shortcuts import render
from Services.models import *
from .models import About, Site, Testimony

def index(request):
    banners= Banner.objects.all()
    plats = Plat.objects.all()
    about = About.objects.all()
    site = Site.objects.all()
    comments = Testimony.objects.all()
    category = Categorie.objects.all()
    return render(request, 'display/index.html', locals())



def about(request):
    return render(request, 'display/about.html')

def book(request):
    return render(request, 'display/book.html')

def menu(request):
    return render(request, 'display/menu.html')


# Create your views here.
