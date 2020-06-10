from django.urls import path
from .views import mostrar_pastor, casa_oracion



urlpatterns = [
    path('Quienes_Somos/',mostrar_pastor,name='mostrar_pastor'),
    path('CasaOracion/',casa_oracion),
]