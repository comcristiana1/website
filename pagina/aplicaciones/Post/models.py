from django.db import models
from ckeditor.fields import RichTextField




#Tabla Form Oracion_Peticion

class FormularioRecursos(models.Model):
    SELECT_CHOICE=(
        ('Oracion','Oracion'),
        ('Peticion','Peticion'),
    )
    id = models.AutoField(primary_key=True)
    name_person = models.CharField('Nombre de la persona',max_length=100,null= False, blank=False)
    mail_persona = models.EmailField('Correo de la persona',max_length=30,null=False,blank=False)
    section_category = models.CharField(max_length=100,null=False,blank=False,choices=SELECT_CHOICE,default='Oracion')
    title = models.CharField('Titulo de Oración/Petición',max_length=30,null=False,blank=False)
    description= models.CharField('Descripción de la Oración/Petición',max_length=255,null=False,blank=False)
    status = models.BooleanField('Estado Publicado/No_Publicado',default=False)


     

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
    image_ev = models.ImageField('Imagen', upload_to='event_image',blank=True,null=False)
    created_date = models.DateField('Fecha de Creación',auto_now=False,auto_now_add=True)
    status = models.BooleanField('Estado Activado/Desactivado',default=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    
    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s" % (self.event_date,self.event_time,self.primary_street,self.secondary_street,self.house_number,self.city,self.description,self.created_date, self.status)



class CasaOracion(models.Model):
    id = models.AutoField("Id",primary_key=True)
    place = models.CharField("Lugar de Reunion", max_length=100, null=True)
    responsable = models.CharField("Responsable", max_length=100, null=True)
    frecuency = models.CharField("Frecuencia", max_length=50)
    day = models.CharField("Dia", max_length=50)
    initial_time = models.TimeField("Hora inicio", auto_now=False, auto_now_add=False)
    final_time = models.TimeField("Hora fin", auto_now=False, auto_now_add=False)
    description = models.TextField("Descripcion", null=False, blank=True)

    class Meta:
        verbose_name = 'Casa Oracion'
        verbose_name_plural = 'Casa Oraciones'

    def __str__(self):
        return "%s %s %s %s %s %s %s %s" % (self.id,self.place,self.responsable,self.frecuency,self.day,self.initial_time,self.final_time,self.description)
    



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

#Creacion tabla Ministerios
class Ministry(models.Model):
    id = models.AutoField(primary_key=True)
    minisName = models.CharField('Nombre Ministerio',max_length=40,null=False,blank=False)
    minisDir = models.CharField('Lugar de Reunión',max_length=100,null=False,blank=False)
    minisPers = models.CharField('Responsable',max_length=80,null=False,blank=False)
    minisFrec = models.CharField('Frecuencia',max_length=20,null=False,blank=False)
    minisCola = models.CharField('Colaboradores',max_length=20,null=False,blank=False)
    minisPhoto = models.ImageField('Imagen Ministerio',upload_to='minis_image',null=False,blank=False)
    minisDesc = models.CharField('Descripción',max_length = 200,null = False, blank = True)
    miniStatus = models.BooleanField('Estado Activado/Desactivado',default = True)

    class Meta:
        verbose_name = 'Ministerios'
        verbose_name_plural = 'Ministerios'

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.minisName,self.minisDir,self.minisPers,self.minisFrec,self.minisCola,self.minisDesc,self.miniStatus)

#Creacion tabla Actividades
class Activities(models.Model):
    id = models.AutoField(primary_key=True)
    actName = models.CharField('Nombre Actividad',max_length=40,null=False,blank=False)
    actPhoto = models.ImageField('Imagen Actividad',upload_to='activ_image',null=False,blank=False)
    actDesc = models.CharField('Descripcion', max_length=200,null=True, blank=True)
    actDate = models.DateField('Fecha Actividad',auto_now=False,auto_now_add=False, null=False, blank=False)
    actTimei = models.TimeField('Hora Inicio',auto_now=False, auto_now_add=False)
    actTimef = models.TimeField('Hora Fin',auto_now=False, auto_now_add=False)
    actDir = models.CharField('Dirección',max_length=100,null=False,blank=False)
    actPers = models.CharField('Encargado', max_length=60, null=False, blank=False)
    actPhono = models.CharField('Teléfono Celular ',max_length = 10, null = True, blank = True)
    actPhono2 = models.CharField('Teléfono Convencional ',max_length = 10, null = True, blank = True)
    actMail = models.EmailField('Correo Electrónico ',max_length = 30,unique = True,null = True, blank = True)
    actStatus = models.BooleanField('Estado Activado/Desactivado',default = True)

    class Meta:
        verbose_name = 'Actividades'
        verbose_name_plural = 'Actividades'
        
    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s %s" % (self.actName,self.actDesc,self.actDate,self.actTimei,self.actTimef,self.actDir,self.actPers,self.actPhono, self.actPhono2, self.actMail, self.actStatus)
        

    


class Recurso(models.Model):
    id = models.AutoField(primary_key=True),
    title = models.CharField("Titulo del PDF", max_length=50,null=False,blank=False)
    pdf = models.FileField(upload_to="Recursos PDF", max_length=254)

    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"

    def __str__(self):
        return self.title

