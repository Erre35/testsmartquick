from django.shortcuts import render
import csv
from django.http import HttpResponse
from rest_framework.views import APIView
from .admin import ClientsResource
from tablib import Dataset

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