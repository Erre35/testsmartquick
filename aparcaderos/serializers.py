from rest_framework import serializers
from .models import Aparcaderos
from .models import Aparcaderos
from buses.serializers import BusesSerializer
from buses.models import Buses

class ShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aparcaderos
        fields = (
            'id',
            'name'
        )

class AparcaderosSerializer(serializers.ModelSerializer):
    buses = serializers.SerializerMethodField('bus_set')

    class Meta:
        model = Aparcaderos
        fields = (
            'id',
            'name',
            'latitud',
            'longitud',
            'capacidad',
            'buses'
        )

    def bus_set(self, aparcadero):
        queryset = Buses.objects.filter(actual_a=aparcadero)
        serializer = BusesSerializer(instance=queryset, many=True)
        return serializer.data