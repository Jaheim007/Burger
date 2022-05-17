from django.contrib import admin
from .models import * 
from django.utils.safestring import mark_safe


@admin.register(Banner)
class about(admin.ModelAdmin):
    list_display = ('title', 'Description',)

@admin.register(Plat)
class Plat(admin.ModelAdmin):
    list_display = ('Nom', 'Description', 'Prix', 'Rprix', 'views', 'Boolean')

    def views(self, obj):     
        return mark_safe(f'<img src="{obj.Image.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images' 

@admin.register(Categorie)
class Category(admin.ModelAdmin):
    list_display = ('nom_de_categorie1', 'nom_de_categorie2', 'nom_de_categorie3','nom_de_categorie4')

@admin.register(OpenDay)
class Days(admin.ModelAdmin):
    list_display = ('Jours', 'Dheure', 'Fheure')



# Register your models here.
