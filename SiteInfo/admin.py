from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

@admin.register(Reservation)
class reserve(admin.ModelAdmin):
    list_display = ('Nom', 'Phone_number', 'Email', 'Jours', 'Maps', 'Person')

@admin.register(About)
class reserve(admin.ModelAdmin):
    list_display = ('Libele', 'Description', 'views')

    def views(self, obj):     
        return mark_safe(f'<img src="{obj.Image.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images' 

@admin.register(Testimony)
class reserve(admin.ModelAdmin):
    list_display = ('Nom', 'Description', 'Metier', 'views',)

    def views(self, obj):     
        return mark_safe(f'<img src="{obj.Image.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images' 

@admin.register(Network)
class reserve(admin.ModelAdmin):
    list_display = ('Nom', 'fb_link', 'insta_link', 'twitter_link', 'views')
        
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.Icon.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images' 



# Register your models here.
