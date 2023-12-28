from django.urls import path, include
from . import views

urlpatterns = [
    
    path('product/<int:pk>', views.Product, name='product'),
    path('category/', views.category, name='category'), 
]
