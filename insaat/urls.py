from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hakkimizda', views.about, name='about'),
    path('servisler', views.service, name='service'),
    path('projeler', views.project, name='project'),
    path('neden_biz', views.feature, name='feature'),
    path('fiyat_teklifi', views.freequote, name='freequote'),
    path('referanslar', views.testimonial, name='testimonial'),
    path('error', views.error, name='error'),
    path('bize_ulasin', views.contact, name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    


