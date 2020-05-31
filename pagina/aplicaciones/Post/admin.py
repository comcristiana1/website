from django.contrib import admin
from .models import Categoria
from .models import Autor
from .models import Miembro

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


admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Miembro,MiembroAdmin)