from django.urls import path, include
from . import views

urlpatterns = [
    
    path('tezgahlar/<int:pk>', views.Product, name='product'),
    path('tezgahlar/', views.category, name='category'), 
    path('doseme/<int:pk>', views.Floor, name='product'), 
    path('doseme/', views.category_floor, name='category_floor'), 
]
