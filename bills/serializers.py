from rest_framework import serializers
from .models import Bills, BillsProducts

class BillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = '__all__'

class BillsProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillsProducts
        fields = '__all__'