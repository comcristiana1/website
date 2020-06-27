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
        return "%s %s %s %s %s %s %s %s %s %s %s %s" % (self.id,self.name1,self.name2,self.surname1,self.surname2,self.ocupation,self.member_image,self.phone1,self.phone2,self.creation_date,self.description,self.status)

Events_Choices = (
    ('Espirituales','Espirituales'),
    ('Sociales','Sociales')
)

class Evento(models.Model):
    id = models.AutoField(primary_key = True)
    category = models.CharField("Categoria",max_length=30,null=False,blank=False,choices=Events_Choices)
    name = models.CharField("Nombre", max_length=100,null=False,blank=False)
    event_date = models.DateField('Fecha del evento',auto_now=False,auto_now_add=False, null=False, blank=False)
    event_time = models.TimeField('Hora del Evento',auto_now=False, auto_now_add=False)
    invited = models.CharField('Invitado',max_length=100,null=False, blank=False,default='Ninguno')
    primary_street = models.CharField('Calle principal',max_length=100,null=False, blank=False)
    secondary_street = models.CharField('Calle secundaria',max_length=100,null=False, blank=False,default='')
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
    name = models.CharField('Nombre Grupo',max_length = 30,null = False,blank = False)
    group_image = models.ImageField('Imagen Grupo',upload_to='group_image',null=False,blank=False)
    direction = models.CharField('Direccion',max_length=100,null=False,blank=False)
    responsible_person = models.CharField('Responsable',max_length=80,null=False,blank=False)
    frequency = models.CharField('Frecuencia',max_length=20,null=False,blank=False)
    date = models.DateField('Fecha',auto_now=False,auto_now_add=False, null=False, blank=False)
    initial_hour = models.TimeField('Hora Inicio',auto_now=False, auto_now_add=False)
    finish_hour = models.TimeField('Hora Fin',auto_now=False, auto_now_add=False)
    collaborators = models.CharField('Colaboradores',max_length=20,null=False,blank=False)
    status = models.BooleanField('Estado Activado/Desactivado',default = True)

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s" % (self.name,self.group_image,self.direction,self.responsible_person,self.frequency,self.date,self.initial_hour,self.finish_hour,self.collaborators,self.status)

#Creacion tabla Ministerios
class Ministry(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre Ministerio',max_length=40,null=False,blank=False)
    direction = models.CharField('Lugar de Reunión',max_length=100,null=False,blank=False)
    responsible_person = models.CharField('Responsable',max_length=80,null=False,blank=False)
    frequency = models.CharField('Frecuencia',max_length=20,null=False,blank=False)
    collaborators = models.CharField('Colaboradores',max_length=20,null=False,blank=False)
    ministry_image = models.ImageField('Imagen Ministerio',upload_to='minis_image',null=False,blank=False)
    description = models.CharField('Descripción',max_length = 200,null = False, blank = True)
    status = models.BooleanField('Estado Activado/Desactivado',default = True)

    class Meta:
        verbose_name = 'Ministerios'
        verbose_name_plural = 'Ministerios'

    def __str__(self):
        return "%s %s %s %s %s %s %s %s" % (self.name,self.direction,self.responsible_person,self.frequency,self.collaborators,self.ministry_image,self.description,self.status)

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
        return "%s %s %s %s %s %s %s %s %s %s %s %s" % (self.name,self.activity_image,self.description,self.date,self.initial_hour,self.finish_hour,self.direction,self.in_charge,self.phone1, self.phone2, self.mail, self.status)
        
#Creación tabla Contacto
class Contactos(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre',max_length=40,null=False,blank=False)
    surname = models.CharField('Apellido',max_length=40,null=False,blank=False)
    mail = models.EmailField('Correo Electrónico ',max_length = 40,unique = True,null = False, blank = False)
    message = models.TextField('Mensaje',blank=False,null=False);
    status = models.BooleanField('Estado Activado/Desactivado',default = True)
    
    class Meta:
        verbose_name = 'Contactos'
        verbose_name_plural = 'Contactos'
        
    def __str__(self):
        return "%s %s %s %s %s" % (self.name,self.surname,self.mail,self.message,self.status)

class Recurso(models.Model):
    id = models.AutoField(primary_key=True),
    title = models.CharField("Titulo del PDF", max_length=50,null=False,blank=False)
    description_r =RichTextField()
    pdf = models.FileField(upload_to="Recursos PDF", max_length=254)

    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"

    def __str__(self):
        return self.title


#Creacion tabla edificadores
class Edificadores(models.Model):
    id = models.AutoField(primary_key=True)
    tipe = models.CharField("Tipo", max_length=15, null=False, blank=False)
    name = models.CharField("Nombre", max_length=80, null=False, blank=False)
    mail = models.EmailField("Email", max_length=50, null=False, blank=False)
    description = models.CharField('Descripcion', max_length=200,null=False, blank=False)

    class Meta:
        verbose_name = "Edificadores"
        verbose_name_plural = "Edificadores"

    def __str__(self):
        return "%s %s %s %s" % (self.tipe,self.name,self.mail,self.description)



#Creacio tabla categoria de un POST

class CategoriaPost(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Nombre de la Categoria',max_length=100,null=False,blank=False)
    status = models.BooleanField('Categoria Activada/Categoria no Activada', default=True)
    create_date = models.DateField('Fecha de Creación',auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name = 'CategoriaPost'
        verbose_name_plural = 'CategoriasPosts'

    def __str__(self):
        return self.name


class AutorPost(models.Model):
    id = models.AutoField(primary_key=True)
    firts_name = models.CharField('Nombres de Autor',max_length=255,null=False,blank=False)
    last_name= models.CharField('Apellidos de Autor',max_length=255,null=False,blank=False)
    mail = models.EmailField('Correo Electronico',null=False,blank=False)
    status = models.BooleanField('Autor Activo/No Activo',default=True)
    create_date = models.DateField('Fecha de creación',auto_now=False,auto_now_add=True)


    class Meta:
        verbose_name='AutorPost'
        verbose_name_plural = 'AutoresPosts'
    
    def __str__(self):
        return "{0},{1}".format(self.last_name,self.firts_name)


class PostBlog(models.Model):
    id = models.AutoField(primary_key= True)
    title = models.CharField('Titulo',max_length=90,blank=False,null=False)
    slug = models.CharField('Slug',max_length=100,blank=False,null=False)
    description = RichTextField()
    content = RichTextField()
    picture = models.ImageField(upload_to="Post")
    auth_post = models.ForeignKey(AutorPost,on_delete=models.CASCADE)
    category_post = models.ForeignKey(CategoriaPost,on_delete=models.CASCADE)
    status = models.BooleanField('Publicado/No publicado',default=True)
    create_date = models.DateField('Fecha de Creación',auto_now=False,auto_now_add=True)


    class Meta:
        verbose_name = 'PostBlog'
        verbose_name_plural = 'PostsBlog'

    def __str__(self):
        return self.title