from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de la categoria',max_length=100,null=False,blank=False)
    create_date =  models.DateField('Fecha Creación',auto_now=False,auto_now_add=True)
    status = models.BooleanField('Estado Activo/Desactivado',default=True)


    class Meta:
        verbose_name='Categoria'
        verbose_name_plural ='Categorias'

    def __str__(self):
        return self.name



