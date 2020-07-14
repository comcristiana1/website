from django.contrib import admin
from .models import Evento,Groups,Ministry,CasaOracion,FormularioRecursos,Recurso,Contactos,Edificadores,CategoriaPost,AutorPost,PostBlog
from .models import Actividades
from .models import Miembro
from .models import GaleriaEventos,GaleriaMinisterio,GaleriaGrupo

# Register your models here.

@admin.register(CategoriaPost)
class CategoriaPostAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id','name')


@admin.register(AutorPost)
class AutorPostAdmin(admin.ModelAdmin):
    search_fields = ['firts_name','id','last_name']
    list_display = ('id','firts_name','last_name','mail','status')


@admin.register(PostBlog)
class PostBlog(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('id','title','content','picture','auth_post','category_post')





class MiembroAdmin(admin.ModelAdmin):
    search_fields = ['name1']

    list_display = ('id', 'name1', 'name2', 'surname1', 'surname2','phone1','phone2', 'ocupation','status')
    list_editable = ['status']

class EventoAdmin(admin.ModelAdmin):
    search_fields = ['event_date']

    list_display = ('id','name','event_date','event_time','primary_street','secondary_street','house_number','city','description','image_ev','created_date','status')

@admin.register(CasaOracion)
class CasaOracionAdmin(admin.ModelAdmin):
    list_display= ('id','title','author','prayer','created_date','status')
    list_editable=['title','author','status']



class GruposAdmin(admin.ModelAdmin):
    search_fields = ['name']

    list_display = ('id','name','group_image','direction','responsible_person','frequency','date','initial_hour','finish_hour','collaborators','status')


class MinisterioAdmin(admin.ModelAdmin):
    search_fields = ['name']

    list_display = ('id','name','direction','responsible_person','frequency','collaborators','ministry_image','description','status')


class ActividadesAdmin(admin.ModelAdmin):
    search_fields = ['name']

    list_display = ('id', 'name', 'activity_image', 'description', 'day', 'frecuency' ,'initial_hour', 'finish_hour', 'direction', 'in_charge', 'phone1', 'phone2', 'mail', 'status')


class FormularioRecursosAdmin(admin.ModelAdmin):
    search_fields = ['section_category','title']
    list_display = ('title','name_person','section_category','mail_persona','description','status')
    list_editable = ['status']

class ContactosAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','surname','mail','message','status')


class RecursoAdmin(admin.ModelAdmin):
    search_fields = ['id','title']
    list_display = ('id','title','pdf')
    
class EdificadoresAdmin(admin.ModelAdmin):
    search_fields = ['tipe','name']
    list_display = ('id','tipe','name','mail','description')




@admin.register(GaleriaMinisterio)
class GaleriaActividadesAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('id','title','image')   

@admin.register(GaleriaGrupo)
class GaleriaActividadesAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('id','title','image')    


@admin.register(GaleriaEventos)
class GaleriaActividadesAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('id','title','image')    



admin.site.register(Miembro,MiembroAdmin)
admin.site.register(Evento,EventoAdmin)
admin.site.register(Groups,GruposAdmin)
admin.site.register(Ministry,MinisterioAdmin)
admin.site.register(Actividades,ActividadesAdmin)
admin.site.register(FormularioRecursos,FormularioRecursosAdmin)
admin.site.register(Recurso,RecursoAdmin)
admin.site.register(Contactos,ContactosAdmin)
admin.site.register(Edificadores,EdificadoresAdmin)