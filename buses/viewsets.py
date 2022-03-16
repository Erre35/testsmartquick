from rest_framework import viewsets
from . import models
from . import serializers

class BusesViewset(viewsets.ModelViewSet):
    queryset = models.Buses.objects.all()
    serializer_class = serializers.BusesSerializer
