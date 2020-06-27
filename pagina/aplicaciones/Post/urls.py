from django.urls import path


from aplicaciones.Post import views

urlpatterns = [
    path('quienes_somos/',views.mostrar_pastor,name='Quienes_Somos'),
    path('casaoracion/',views.casa_oracion,name='Casa_de_Oracion'),
    path('actividades/',views.mostrar_actividades,name='Actividades'),
    path('ministerio/',views.mostrar_ministerio,name='Ministerios'),
    path('recursos/',views.oracion_peticion,name='Recursos'),
    path('eventos/',views.mostrar_eventos,name='Eventos'),
    path('eventos-espirituales/',views.mostrar_eventosEspirituales,name='Eventos_Espirituales'),
    path('eventos-sociales/',views.mostrar_eventosSociales,name='Eventos_Sociales'),
    path('grupos/',views.mostrar_grupos,name='Grupos'),
    path('oracion/',views.mostrar_oracion,name='Oracion'),
    path('peticion/',views.mostrar_peticion,name='Peticion'),
    path('contactos/',views.mostrar_contactos,name='Contactos'),
    path('edificadores/',views.mostrar_edificadores,name='Edificadores')
]