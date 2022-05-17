from django.db import models

class Reservation(models.Model):
    Nom = models.CharField(max_length=255)
    Phone_number= models.CharField(max_length=255)
    Email = models.EmailField(max_length=254)
    Jours = models.DateField()
    Maps = models.URLField()
    Person = models.IntegerField()

class About(models.Model):
    Libele = models.CharField(max_length=255)
    Description = models.TextField(max_length=500)
    Image = models.ImageField()

class Testimony(models.Model):
    Nom = models.CharField(max_length=255)
    Image = models.ImageField()
    Description = models.TextField(max_length=500)
    Metier = models.CharField(max_length=255)

class Network(models.Model):
    Icon = models.ImageField()
    Nom = models.CharField(max_length=255)
    fb_link = models.URLField()
    insta_link = models.URLField()
    twitter_link = models.URLField()

class Site(models.Model):
    tilte = models.ImageField()
    copyright = models.TextField()
    Section_banner_image = models.ImageField()
    Description_footer = models.TextField()






# Create your models here.
