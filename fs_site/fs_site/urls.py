from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('main.urlsFacesOfWarCountries')),
    path('', include('main.urlsQuotesTypes')),
    path('', include('main.urlsService'))
]
