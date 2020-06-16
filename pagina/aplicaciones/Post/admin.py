from django.contrib import admin
from .models import Evento,Groups,Ministry,CasaOracion,FormularioRecursos,Recurso
from .models import Actividades
from .models import Miembro

# Register your models here.







class MiembroAdmin(admin.ModelAdmin):
    search_fields = ['name1']

    list_display = ('id', 'name1', 'name2', 'surname1', 'surname2', 'ocupation', 'member_image','phone1','phone2', 'creation_date', 'description','status')


class EventoAdmin(admin.ModelAdmin):
    search_fields = ['event_date']

    list_display = ('id','event_date','event_time','primary_street','secondary_street','house_number','city','description','image_ev','created_date','status')

@admin.register(CasaOracion)
class CasaOracionAdmin(admin.ModelAdmin):
    list_display= ('id','place','responsable','frecuency','day','initial_time','final_time','description')



class GruposAdmin(admin.ModelAdmin):
    search_fields = ['groupName']

    list_display = ('id','groupName','groupDir')


class MinisterioAdmin(admin.ModelAdmin):
    search_fields = ['minisName']

    list_display = ('id','minisName','minisDir','minisPers','minisFrec','minisCola','minisPhoto','minisDesc','miniStatus')


class ActividadesAdmin(admin.ModelAdmin):
    search_fields = ['name']

    list_display = ('id', 'name', 'activity_image', 'description', 'date', 'initial_hour', 'finish_hour', 'direction', 'in_charge', 'phone1', 'phone2', 'mail', 'status')


class FormularioRecursosAdmin(admin.ModelAdmin):
    search_fields = ['section_category','title']
    list_display = ('title','name_person','section_category','mail_persona','description','status')



class RecursoAdmin(admin.ModelAdmin):
    search_fields = ['id','title']
    list_display = ('id','title','pdf')
    





admin.site.register(Miembro,MiembroAdmin)
admin.site.register(Evento,EventoAdmin)
admin.site.register(Groups,GruposAdmin)
admin.site.register(Ministry,MinisterioAdmin)
admin.site.register(Actividades,ActividadesAdmin)
admin.site.register(FormularioRecursos,FormularioRecursosAdmin)
admin.site.register(Recurso,RecursoAdmin)