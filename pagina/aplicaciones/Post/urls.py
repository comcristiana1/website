from django.urls import path
from .views import mostrar_pastor, casa_oracion,oracion,oracion_peticion,mostrar_actividades,mostrar_ministerio



urlpatterns = [
    path('Quienes_Somos/',mostrar_pastor,name='mostrar_pastor'),
    path('CasaOracion/',casa_oracion),
    path('Oracion/',oracion,name='orar'),
    path('Actividades/', mostrar_actividades),
    path('Ministerio/',mostrar_ministerio),
    path('prueba/',oracion_peticion),
]