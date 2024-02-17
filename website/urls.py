
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

from schema_graph.views import Schema


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('insaat.urls')),
    path('urunler/', include('urunler.urls')),
    path("schema/", Schema.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'insaat.views.error'
