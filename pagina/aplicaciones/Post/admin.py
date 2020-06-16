from django.contrib import admin
from .models import Miembro,Evento,Groups,Ministry,Activities,CasaOracion,FormularioRecursos,Recurso


# Register your models here.







class MiembroAdmin(admin.ModelAdmin):
    search_fields = ['miemName1']

    list_display = ('id', 'miemName1', 'miemName2', 'miemSurname1', 'miemSurname2', 'miemOcu', 'miemPho1', 'miemPho2', 'miemCrea', 'miemDesc')


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
    search_fields = ['actName']

    list_display = ('id', 'actName', 'actPhoto', 'actDesc', 'actDate', 'actTimei', 'actTimef', 'actDir', 'actPers', 'actPhono', 'actPhono2', 'actMail', 'actStatus')


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
admin.site.register(Activities,ActividadesAdmin)
admin.site.register(FormularioRecursos,FormularioRecursosAdmin)
admin.site.register(Recurso,RecursoAdmin)