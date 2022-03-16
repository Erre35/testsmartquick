from numpy import product
from rest_framework import serializers
from .models import Bills, BillsProducts
from products.serializers import ProductsSerializer
from clients.serializers import ClientsSerializer

class BillsSerializer(serializers.ModelSerializer):
    client = ClientsSerializer(many=False)
    product = ProductsSerializer(many=False)
    class Meta:
        model = Bills
        fields = '__all__'

class BillsProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillsProducts
        fields = '__all__'