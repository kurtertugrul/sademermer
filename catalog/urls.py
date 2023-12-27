from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
# from .views import download_catalog



urlpatterns = [
    path('catalog_granite', views.catalog_granite, name='catalog_granite'),
    path('catalog_belenco', views.catalog_belenco, name='catalog_belenco'),
    path('catalog_cimstone', views.catalog_cimstone, name='catalog_cimstone'),
    path('catalog_calisco', views.catalog_calisco, name='catalog_calisco'),
    path('catalog_granite_kitchen', views.catalog_granite_kitchen, name='catalog_granite_kitchen'),
    path('catalog_marble', views.catalog_marble, name='catalog_marble'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
