from django.db import models

class Reservation(models.Model):
    Nom = models.CharField(max_length=255)
    dial_code = models.CharField(max_length=4)
    Phone_number= models.CharField(max_length=10)
    Email = models.EmailField(max_length=254)
    Jours = models.DateField()
    Maps = models.URLField(max_length=255)
    Person = models.IntegerField()
    
    def __str__(self): 
        return self.Nom

class About(models.Model):
    Libele = models.CharField(max_length=255)
    Description = models.TextField(max_length=500)
    Image = models.FileField()
    
    def __str__(self): 
        return self.Libele

class Testimony(models.Model):
    Nom = models.CharField(max_length=255)
    Image = models.FileField()
    Description = models.TextField(max_length=500)
    Metier = models.CharField(max_length=255)
    
    def __str__(self): 
        return self.Nom

class Network(models.Model):
    Nom = models.CharField(max_length=255)
    fb_link = models.URLField()
    insta_link = models.URLField()
    twitter_link = models.URLField()
    
    def __str__(self): 
        return self.Nom

class Site(models.Model):
    title = models.CharField(max_length=255)
    copyright = models.TextField()
    Section_banner_image = models.FileField()
    Description_footer = models.TextField()
    
    def __str__(self): 
        return self.title






# Create your models here.
