from django.contrib import admin

from import_export import resources
from clients.models import Clients

class ClientsResource(resources.ModelResource):

    class Meta:
        model = Clients