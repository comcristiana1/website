from django.contrib import admin
from .models import Categoria,Autor,Miembro,Evento,Groups,Ministry,Activities,Post


# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['name']

    list_display = ('id','name','status','create_date')


class AutorAdmin(admin.ModelAdmin):
    search_fields = ['autName1']

    list_display = ('id','autName1','autName2','autSurname1','autSurname2','autMail','autStatus')


class MiembroAdmin(admin.ModelAdmin):
    search_fields = ['miemName1']

    list_display = ('id','miemName1','miemName2','miemSurname1','miemSurname2','miemOcu','miemPho1','miemPho2','miemCrea','miemDesc')


class EventoAdmin(admin.ModelAdmin):
    search_fields = ['event_date']

    list_display = ('id','event_date','event_time','primary_street','secondary_street','house_number','city','description','image','created_date','status')


class GruposAdmin(admin.ModelAdmin):
    search_fields = ['groupName']

    list_display = ('id','groupName','groupDir')


class MinisterioAdmin(admin.ModelAdmin):
    search_fields = ['minisName']

    list_display = ('id','minisName','minisDir','minisPers','minisFrec','minisCola','minisPhoto','minisDesc','miniStatus')


class ActividadesAdmin(admin.ModelAdmin):
    search_fields = ['actName']

    list_display = ('id','actName','actPhoto','actDesc','actDate','actTimei','actTimef','actDir','actPers','actPhono','actPhono2','actMail','actStatus')




admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Miembro,MiembroAdmin)
admin.site.register(Evento,EventoAdmin)
admin.site.register(Groups,GruposAdmin)
admin.site.register(Ministry,MinisterioAdmin)
admin.site.register(Activities,ActividadesAdmin)
admin.site.register(Post)