from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=255)
    Description = models.TextField(max_length=500)

class Plat(models.Model):
    Nom = models.CharField(max_length=255)
    Description = models.TextField(max_length=500)
    Image = models.FileField()
    Prix = models.CharField(max_length=255)
    Rprix = models.CharField(max_length=255)
    Boolean = models.BooleanField()

class Categorie(models.Model):
    nom_de_categorie1 = models.CharField(max_length=255)
    nom_de_categorie2 = models.CharField(max_length=255)
    nom_de_categorie3 = models.CharField(max_length=255)
    nom_de_categorie4 = models.CharField(max_length=255)

class OpenDay(models.Model):
    Jours = models.CharField(max_length=255)
    Dheure = models.TimeField(auto_now=False, auto_now_add=False)
    Fheure = models.TimeField(auto_now=False, auto_now_add=False)
    


# Create your models here.
