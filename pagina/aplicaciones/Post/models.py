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
class Miembro(models.Model):
    id = models.AutoField(primary_key = True)
    name1 = models.CharField('Primer Nombre',max_length = 30,null = False,blank = False)
    name2 = models.CharField('Segundo Nombre',max_length = 30,null = True,blank = True)
    surname1 = models.CharField('Primer Apellido',max_length = 30,null = False,blank = False)
    surname2 = models.CharField('Segundo Apellido',max_length = 30,null = True,blank = True)
    ocupation = models.CharField('Ocupación',max_length = 30,null = False, blank = False)
    member_image = models.ImageField('Imagen', upload_to='member_image',blank=True,null=False) 
    phone1 = models.CharField('Teléfono Convencional',max_length = 10,null = True, blank = True)
    phone2 = models.CharField('Teléfono Celular',max_length = 10, null = True, blank = True)
    creation_date = models.DateField('Fecha de Creación',auto_now=False,auto_now_add=True)
    description = models.CharField('Descripción',max_length = 200,null = True, blank = True)
    status = models.BooleanField('Estado Publicado/No_Publicado',default=False)

    class Meta:
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'
    
    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s" % (self.name1,self.name2,self.surname1,self.surname2,self.ocupation,self.member_image,self.phone1,self.phone2,self.creation_date,self.description)

class Evento(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField("Nombre", max_length=100,null=False,blank=False)
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
        return "%s %s %s %s %s %s %s %s %s %s %s" % (self.name,self.event_date,self.event_time,self.primary_street,self.secondary_street,self.house_number,self.city,self.description,self.image_ev,self.created_date, self.status)



class CasaOracion(models.Model):
    id = models.AutoField("Id",primary_key=True)
    title = models.CharField("Titulo", max_length=100,null=False,blank=False)
    author = models.CharField("Autor", max_length=100, null=False,blank=False)
    prayer = models.TextField("Oracion", max_length=500,null=False, blank=False)
    created_date = models.DateField('Fecha de Creación',auto_now=False,auto_now_add=True)
    status = models.BooleanField('Estado Activado/Desactivado',default=True)

    class Meta:
        verbose_name = 'Casa Oracion'
        verbose_name_plural = 'Casa Oraciones'

    def __str__(self):
        return "%s %s %s %s %s %s" % (self.id,self.title,self.author,self.prayer,self.created_date,self.status)
    



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
class Actividades(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre Actividad',max_length=40,null=False,blank=False)
    activity_image = models.ImageField('Imagen Actividad',upload_to='activ_image',null=False,blank=True)
    description = models.CharField('Descripcion', max_length=200,null=True, blank=True)
    date = models.DateField('Fecha Actividad',auto_now=False,auto_now_add=False, null=False, blank=False)
    initial_hour = models.TimeField('Hora Inicio',auto_now=False, auto_now_add=False)
    finish_hour = models.TimeField('Hora Fin',auto_now=False, auto_now_add=False)
    direction = models.CharField('Dirección',max_length=100,null=False,blank=False)
    in_charge = models.CharField('Encargado', max_length=60, null=False, blank=False)
    phone1 = models.CharField('Teléfono Celular ',max_length = 10, null = True, blank = True)
    phone2 = models.CharField('Teléfono Convencional ',max_length = 10, null = True, blank = True)
    mail = models.EmailField('Correo Electrónico ',max_length = 30,unique = True,null = True, blank = True)
    status = models.BooleanField('Estado Activado/Desactivado',default = True)

    class Meta:
        verbose_name = 'Actividades'
        verbose_name_plural = 'Actividades'
        
    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s %s" % (self.name,self.activity_image,self.description,self.date,self.initial_hour,self.finish_hour,self.direction,self.in_charge,self.phone1, self.phone2, self.mail, self.status)
        

    


class Recurso(models.Model):
    id = models.AutoField(primary_key=True),
    title = models.CharField("Titulo del PDF", max_length=50,null=False,blank=False)
    pdf = models.FileField(upload_to="Recursos PDF", max_length=254)

    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"

    def __str__(self):
        return self.title

