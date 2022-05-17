from django.shortcuts import render
from Services.models import *

def index(request):
    ban = Banner.objects.filter().first
    banners= Banner.objects.all()

    return render(request, 'display/index.html', locals())



def about(request):
    return render(request, 'display/about.html')

def book(request):
    return render(request, 'display/book.html')

def menu(request):
    return render(request, 'display/menu.html')


# Create your views here.
