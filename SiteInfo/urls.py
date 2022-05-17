from django.urls import path
from .views import *

urlpatterns = [
    path('', index , name="index" ),
    path('about', about , name="about" ),
    path('book', book , name="book" ),
    path('menu', menu , name="menu" )
]