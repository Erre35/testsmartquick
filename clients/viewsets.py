from rest_framework import viewsets
from . import models
from . import serializers

class ClientsViewset(viewsets.ModelViewSet):
    queryset = models.Clients.objects.all()
    serializer_class = serializers.ClientsSerializer
