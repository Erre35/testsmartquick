from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    def __str__(self):
        return self.name
