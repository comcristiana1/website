from django.contrib import admin
from .models import Categoria

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['name']

    list_display = ('id','name','status','create_date')



admin.site.register(Categoria,CategoriaAdmin)
