from django.contrib import admin
from .models import * 
from django.utils.safestring import mark_safe

@admin.register(Banner)
class About(admin.ModelAdmin):
    list_display = ('title', 'Description',)

@admin.register(Plat)
class Plat(admin.ModelAdmin):
    list_display = ('views', 'Nom', 'Description', 'category', 'Prix', 'Rprix', 'Boolean')

    def views(self, obj):     
        return mark_safe(f'<img src="{obj.Image.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images' 

@admin.register(Categorie)
class Category(admin.ModelAdmin):
    list_display = ('Name',)

@admin.register(OpenDay)
class Days(admin.ModelAdmin):
    list_display = ('Jours', 'Dheure', 'Fheure')



# Register your models here.
