from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

@admin.register(Reservation)
class Reserve(admin.ModelAdmin):
    list_display = ('Nom', 'Phone_number', 'Email', 'Jours', 'Maps', 'Person')

@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('views', 'Libele', 'Description', )

    def views(self, obj):     
        return mark_safe(f'<img src="{obj.Image.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images' 

@admin.register(Testimony)
class Testimony(admin.ModelAdmin):
    list_display = ('views','Nom', 'Description', 'Metier', )

    def views(self, obj):     
        return mark_safe(f'<img src="{obj.Image.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images' 

@admin.register(Network)
class Network(admin.ModelAdmin):
    list_display = ('Nom', 'fb_link', 'insta_link', 'twitter_link' )

@admin.register(Site) 
class Site(admin.ModelAdmin):  
    list_display = ('views','title', 'Description_footer', 'copyright')
    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.Section_banner_image.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images' 
    
# Register your models here.
