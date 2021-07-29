from django.db import models

# Create your models here.
class Clients(models.Model):
    document = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    def __str__(self):
        return self.first_name + " " + self.last_name