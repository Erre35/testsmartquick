from rest_framework import serializers
from .models import Buses
# from aparcaderos.serializers import AparcaderosSerializer
import aparcaderos.serializers as serialAparcaderos

class BusesSerializer(serializers.ModelSerializer):
    # origen = serialAparcaderos.ShortSerializer()
    class Meta:
        model = Buses
        fields = '__all__'