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


#Creacion Tabla Eventos
#Hecho por Andres Cevallos
class Evento(models.Model):
    id = models.AutoField(primary_key = True)
    event_date = models.DateField('Fecha del evento',auto_now=False,auto_now_add=False, null=False, blank=False)
    event_time = models.TimeField('Hora del Evento',auto_now=False, auto_now_add=False)
    primary_street = models.CharField('Calle principal',max_length=100,null=False, blank=False)
    secondary_street = models.CharField('Calle secundaria',max_length=100,null=True, blank=True)
    house_number = models.CharField('Numero Domicilio',max_length=100,null=False, blank=False)
    city = models.CharField('Ciudad',max_length=50,null=False,blank=False)
    description = models.TextField(max_length=200,null=False, blank=False)
    image = models.ImageField('Imagen', upload_to='event_image',blank=True,null=False)
    created_date = models.DateField('Fecha de Creación',auto_now=False,auto_now_add=True)
    status = models.BooleanField('Estado Activado/Desactivado',default=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    
    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s" % (self.event_date,self.event_time,self.primary_street,self.secondary_street,self.house_number,self.city,self.description,self.created_date, self.status)

class Groups(models.Model):
    id = models.AutoField(primary_key=True)
    groupName = models.CharField('Nombre Grupo',max_length = 30,null = False,blank = False)
    grouPhoto = models.ImageField('Imagen Grupo',upload_to='group_image',null=False,blank=False)
    groupDir = models.CharField('Direccion',max_length=100,null=False,blank=False)
    groupStatus = models.BooleanField('Estado Activado/Desactivado',default = True)

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return "%s %s" % (self.groupName,self.groupDir)

class Ministry(models.Model):
    id = models.AutoField(primary_key=True)
    minisName = models.CharField('Nombre Ministerio',max_length=40,null=False,blank=False)
    minisPhoto = models.ImageField('Imagen Ministerio',upload_to='minis_image',null=False,blank=False)
    minisDir = models.CharField('Direccion',max_length=100,null=False,blank=False)
    miniStatus = models.BooleanField('Estado Activado/Desactivado',default = True)

    class Meta:
        verbose_name = 'Ministerios'
        verbose_name_plural = 'Ministerios'

    def __str__(self):
        return "%s %s" % (self.minisName,self.minisDir)
