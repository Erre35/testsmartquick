from rest_framework import viewsets
from . import models
from . import serializers

class AparcaderosViewset(viewsets.ModelViewSet):
    queryset = models.Aparcaderos.objects.all()
    serializer_class = serializers.AparcaderosSerializer
