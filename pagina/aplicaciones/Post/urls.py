from django.urls import path
from .views import mostrar_pastor, casa_oracion,oracion_peticion,mostrar_actividades,mostrar_ministerio,mostrar_eventos,mostrar_grupos



urlpatterns = [
    path('quienes_somos/',mostrar_pastor,name='Quienes_Somos'),
    path('casaoracion/',casa_oracion,name='Casa_de_Oracion'),
    path('actividades/', mostrar_actividades,name='Actividades'),
    path('ministerio/',mostrar_ministerio,name='Ministerios'),
    path('recursos/',oracion_peticion,name='Recursos'),
    path('eventos/',mostrar_eventos,name='Eventos'),
    path('grupos/',mostrar_grupos,name='Grupos'),
]