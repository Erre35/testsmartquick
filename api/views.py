from django.shortcuts import render
import csv
from django.http import HttpResponse
from rest_framework.views import APIView
from aparcaderos.models import Aparcaderos
from buses.models import Buses
from aparcaderos.serializers import AparcaderosSerializer
from .admin import ClientsResource
from tablib import Dataset
from datetime import datetime
from rest_framework.response import Response


class exportCsvClients(APIView):
    def get(self, request, *args, **kwargs):
        dataset = ClientsResource().export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        return response

def importCsvClients(request):
    if request.method == 'POST':
        clients_resource = ClientsResource()
        dataset = Dataset()
        new_clients = request.FILES['clientsFile']
        imported_data = dataset.load(new_clients.read().decode(),format='csv')
        result = clients_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            clients_resource.import_data(dataset, dry_run=False)
            return render(request, 'uploadClientsSuccessful.html')


    return render(request, 'uploadClients.html')

class updateBusState(APIView):
    def get(self, format=None):
        now = datetime.now()
        print("now ", now)
        aparcaderos = Buses.objects.filter(hora_llegada__lte=now)
        print("aparcaderos ", aparcaderos)
        
        for app in aparcaderos:
            print("app.id ", app.id)

            Buses.objects.filter(id=app.id).update(actual_a=app.llegada)

        # for ap in aparcaderos:
        #     print("ap.hora_llegada ", ap.hora_llegada)
        #     if ap.hora_llegada > now:
        #         Buses.objects.filter(id = ap.id).update(actual_a=ap.llegada)
        aparcaderos = Aparcaderos.objects.all()
        serializer = AparcaderosSerializer(aparcaderos, many=True)
        return Response(serializer.data)
