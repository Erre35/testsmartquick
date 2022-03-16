from django.conf.urls import url
import aparcaderos.views as apiView

urlpatterns = [
    url(r'^mapa$', apiView.mapa, name='mapa'),
]
