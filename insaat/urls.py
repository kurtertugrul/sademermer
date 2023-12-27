from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('project', views.project, name='project'),
    path('feature', views.feature, name='feature'),
    path('freequote', views.freequote, name='freequote'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('error', views.error, name='error'),
    path('contact', views.contact, name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    


