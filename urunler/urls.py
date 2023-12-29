from django.urls import path, include
from . import views

urlpatterns = [
    
    path('product/<int:pk>', views.Product, name='product'),
    path('category/', views.category, name='category'), 
    path('floor/<int:pk>', views.Floor, name='product'), 
    path('category_floor/', views.category_floor, name='category_floor'), 
]
