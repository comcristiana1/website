from django.urls import path
from .views import mostrar_pastor



urlpatterns = [
    path('Quienes_Somos/',mostrar_pastor,name='mostrar_pastor'),
    
]