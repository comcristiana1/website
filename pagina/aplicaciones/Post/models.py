from django.db import models

# Creación tabla Categoria
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de la categoria',max_length=100,null=False,blank=False)
    create_date =  models.DateField('Fecha Creación',auto_now=False,auto_now_add=True)
    status = models.BooleanField('Estado Activado/Desactivado',default=True)


    class Meta:
        verbose_name='Categoria'
        verbose_name_plural ='Categorias'

    def __str__(self):
        return self.name

#Creación tabla Autor
#Hecho por: Jorge Hidalgo
class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    autName1 = models.CharField('Primer Nombre',max_length = 30, null = False, blank = False)
    autName2 = models.CharField('Segundo Nombre',max_length = 30, null = True, blank = True)
    autSurname1 = models.CharField('Primer Apellido',max_length = 30,null = False, blank = False)
    autSurname2 = models.CharField('Segundo Apellido',max_length = 30,null = True, blank = True)
    autMail = models.EmailField('Correo Electrónico',max_length = 30,unique = True,null = True, blank = True)
    autStatus = models.BooleanField('Estado Activado/Desactivado',default = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "%s %s %s %s %s" % (self.autName1,self.autName2,self.autSurname1,self.autSurname2,self.autMail)        

#Creación tabla Miembro
#Hecho por: Jorge Hidalgo
class Miembro(models.Model):
    id = models.AutoField(primary_key = True)
    miemName1 = models.CharField('Primer Nombre',max_length = 30,null = False,blank = False)
    miemName2 = models.CharField('Segundo Nombre',max_length = 30,null = True,blank = True)
    miemSurname1 = models.CharField('Primer Apellido',max_length = 30,null = False,blank = False)
    miemSurname2 = models.CharField('Segundo Apellido',max_length = 30,null = True,blank = True)
    miemOcu = models.CharField('Ocupación',max_length = 30,null = False, blank = False)
    #miemIma = models.ImageField(upload_to = ) 
    miemPho1 = models.CharField('Teléfono Convencional',max_length = 10,null = True, blank = True)
    miemPho2 = models.CharField('Teléfono Celular',max_length = 10, null = True, blank = True)
    miemCrea = models.DateField('Fecha de Creación',auto_now=False,auto_now_add=True)
    miemDesc = models.CharField('Descripción',max_length = 200,null = True, blank = True)

    class Meta:
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'
    
    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s" % (self.miemName1,self.miemName2,self.miemSurname1,self.miemSurname2,self.miemOcu,self.miemPho1,self.miemPho2,self.miemCrea,self.miemDesc)