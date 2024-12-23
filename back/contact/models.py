from django.db import models

# Create your models here.

class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    numero = models.CharField(max_length=20)
    statut = models.CharField(max_length=100)
    message = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
