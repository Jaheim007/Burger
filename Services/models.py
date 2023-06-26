from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=255)
    Description = models.TextField(max_length=500)
class Categorie(models.Model):
    Name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Name

class Plat(models.Model):
    Nom = models.CharField(max_length=255)
    Description = models.TextField(max_length=500)
    Image = models.FileField()
    Prix = models.CharField(max_length=255)
    Rprix = models.CharField(max_length=255)
    Boolean = models.BooleanField()
    category = models.ForeignKey(Categorie , on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.Nom
    
    
class OpenDay(models.Model):
    Jours = models.CharField(max_length=255)
    Dheure = models.TimeField(auto_now=False, auto_now_add=False)
    Fheure = models.TimeField(auto_now=False, auto_now_add=False)
    


# Create your models here.
