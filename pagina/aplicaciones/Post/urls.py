from django.urls import path
from .views import mostrar_pastor,mostrar_contactos, casa_oracion,oracion_peticion,mostrar_actividades,mostrar_ministerio,mostrar_eventos,mostrar_eventosEspirituales,mostrar_eventosSociales,mostrar_grupos
from .views import mostrar_oracion,mostrar_peticion


urlpatterns = [
    path('quienes_somos/',mostrar_pastor,name='Quienes_Somos'),
    path('casaoracion/',casa_oracion,name='Casa_de_Oracion'),
    path('actividades/', mostrar_actividades,name='Actividades'),
    path('ministerio/',mostrar_ministerio,name='Ministerios'),
    path('recursos/',oracion_peticion,name='Recursos'),
    path('eventos/',mostrar_eventos,name='Eventos'),
    path('eventos-espirituales/',mostrar_eventosEspirituales,name='Eventos_Espirituales'),
    path('eventos-sociales/',mostrar_eventosSociales,name='Eventos_Sociales'),
    path('grupos/',mostrar_grupos,name='Grupos'),
    path('oracion/', mostrar_oracion,name='Oracion'),
    path('peticion/',mostrar_peticion,name='Peticion'),
    path('contactos/',mostrar_contactos,name='Contactos'),
]