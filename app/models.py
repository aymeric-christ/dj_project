from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100,default="")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    niveau_etude = models.CharField(max_length=100,default="")
    etablissement_origine = models.CharField(max_length=100,default="")
    concours_souhaite = models.CharField(max_length=100,default="")


    def __str__(self):
        return self.name