from django.db import models
from aparcaderos.models import Aparcaderos

# Create your models here.
class Buses(models.Model):
    placa = models.CharField(max_length=150)
    hora_salida = models.DateTimeField()
    hora_llegada = models.DateTimeField()
    origen = models.ForeignKey(
                    Aparcaderos, null=True, 
                    on_delete=models.CASCADE,
                    related_name='buses_origen')
    llegada = models.ForeignKey(
                    Aparcaderos, null=True, 
                    on_delete=models.CASCADE,
                    related_name='buses_llegada')
    actual_a = models.ForeignKey(
                    Aparcaderos, null=True, 
                    on_delete=models.CASCADE,
                    related_name='buses_actual_a')
    def __str__(self):
        return self.placa