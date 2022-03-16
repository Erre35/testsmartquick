from django.db import models

# Create your models here.
class Aparcaderos(models.Model):
    name = models.CharField(max_length=150)
    latitud = models.CharField(max_length=150)
    longitud = models.CharField(max_length=150)
    capacidad = models.CharField(max_length=150)
    def __str__(self):
        return self.name