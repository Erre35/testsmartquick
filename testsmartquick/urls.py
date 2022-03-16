from django.contrib import admin
from django.urls import path, include
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('API/', include(('api.urls', "API"), namespace="API")),
    path('aparcaderos/', include(('aparcaderos.urls', "aparcaderos"), namespace="aparcaderos")),
]
