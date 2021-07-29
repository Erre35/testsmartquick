from django.conf.urls import url
import api.views as apiView

urlpatterns = [
    url(r'^exportCsvClients$', apiView.exportCsvClients.as_view(), name='exportCsvClients'),
    url(r'^importCsvClients$', apiView.importCsvClients, name='importCsvClients'),    
]
