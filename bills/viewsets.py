from rest_framework import viewsets
from . import models
from . import serializers

class BillsViewset(viewsets.ModelViewSet):
    queryset = models.Bills.objects.all()
    serializer_class = serializers.BillsSerializer

class BillsProductsViewset(viewsets.ModelViewSet):
    queryset = models.BillsProducts.objects.all()
    serializer_class = serializers.BillsProductsSerializer