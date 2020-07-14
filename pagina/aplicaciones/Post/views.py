from django.shortcuts import render,redirect
from .models import CasaOracion,Ministry,Evento,Groups,Recurso,Contactos,Edificadores
from .models import Actividades
from .models import Miembro
from .models import FormularioRecursos
from .forms import O_PForm,ContactosForm,EdificadoresForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import GaleriaEventos,GaleriaGrupo,GaleriaMinisterio


from .models import PostBlog, CategoriaPost, AutorPost


# Create your views here.



def home(request):
    ultimo = Evento.objects.last()
    aux = Evento.objects.values_list(flat=True).last()
    pen = Evento.objects.all();
    aux = len(pen)
    penultimo = pen[aux-2]

    #evento2 = Evento.objects.filter(creation_date =  ultimo-1)
    return render(request,'base.html',{'ultimo':ultimo,'penultimo':penultimo})



def mostrar_pastor(request):
    mostrar = Miembro.objects.filter(status=True)
    return render(request,'Post/quienessomos.html',{'mostrar':mostrar})

def casa_oracion(request):
    queryset = request.GET.get("buscar")
    oracion = CasaOracion.objects.filter(status=True)
    if queryset:
        oracion = CasaOracion.objects.filter(
            Q(title__icontains=queryset) |
            Q(prayer__icontains=queryset)
        ).distinct()
    if oracion:
        last = len(oracion)-1
        last_prayer = oracion[last]
    else:
        last_prayer=False
    paginator = Paginator(oracion,12)
    page = request.GET.get('page')
    oracion = paginator.get_page(page)
    return render(request,'Post/casa_oracion.html',{'oracion':oracion,'last':last_prayer})





def mostrar_actividades(request):
    actividad = Actividades.objects.filter(status= True)
    return render(request,'Post/actividades.html',{'actividad':actividad})

def mostrar_ministerio(request):
    ministerio = Ministry.objects.all()
    galery = GaleriaMinisterio.objects.filter(status=True)
    return render(request,'POST/ministerios.html',{'ministerio':ministerio,'galeria':galery})    


def oracion_peticion(request):

    libros = Recurso.objects.all()

    if request.method=='POST':
        O_P_form = O_PForm(request.POST)
        if O_P_form.is_valid():
            subject = request.POST["title"]
            message = "Hola soy "+request.POST["name_person"]+" "+request.POST["description"] + " att: " + request.POST["mail_persona"]
            email_from=settings.EMAIL_HOST_USER
            recipient_list = ["adrigato3@gmail.com"]
            send_mail(subject,message,email_from,recipient_list)

            O_P_form.save()
            return redirect('Post:Oracion')
    else:
        O_P_form = O_PForm()

    return render(request,'Post/recursos.html',{'datos':O_P_form,'recursos':libros})


def mostrar_eventos(request):
    eventos = Evento.objects.filter(status= True)

    galeria = GaleriaEventos.objects.filter(status=True)
    return render(request,'POST/eventos.html',{'eventos':eventos,'galeria':galeria})

def mostrar_eventosEspirituales(request):
    eventos = Evento.objects.all().filter(category = 'Espirituales');
    galeria = GaleriaEventos.objects.filter(status=True)
    return render(request,'POST/eventos.html',{'eventos':eventos,'galeria':galeria})   

def mostrar_eventosSociales(request):
    eventos = Evento.objects.all().filter(category = 'Sociales');
    galeria = GaleriaEventos.objects.filter(status=True)
    return render(request,'POST/eventos.html',{'eventos':eventos,'galeria':galeria})

def mostrar_grupos(request):
    grupos = Groups.objects.all()
    galery = GaleriaGrupo.objects.filter(status=True)
    return render(request,'POST/grupos.html',{'grupos':grupos,'galeria':galery})

def mostrar_oracion(request):
    prayer = FormularioRecursos.objects.filter(section_category='Oracion',status=True)
    paginator = Paginator(prayer,20)
    page = request.GET.get('page')
    prayer = paginator.get_page(page)
    return render(request,'Post/oracion.html',{'oracion': prayer,'paginator':paginator})

def mostrar_peticion(request):
    peticion = FormularioRecursos.objects.filter(section_category='Peticion',status=True)
    paginator = Paginator(peticion,20)
    page = request.GET.get('page')
    peticion = paginator.get_page(page)
    return render(request,'Post/peticion.html',{'peticion': peticion,'paginator':paginator})

def mostrar_contactos(request):
    contactos = Contactos.objects.all()
    return render(request,'POST/contactos.html',{'contactos':contactos})

def mostrar_edificadores(request):
    edificadores = Edificadores.objects.all()
    return render(request,'Post/edificadores.html',{'edificadores':edificadores}) 



def contactanos(request):
    if request.method == 'POST':
        datos = ContactosForm(request.POST)
        print(datos)
        if datos.is_valid():
            datos.save()
            return redirect('index')
        else:
            return render(request,'Post/contactos.html',{"error":"Campos no validos"})
    else:
        datos = ContactosForm()
    return render(request,'Post/contactos.html',{"datos":datos})



def edificadores(request):
    if request.method == 'POST':
        datos = EdificadoresForm(request.POST)
        if datos.is_valid():
            datos.save()
            return redirect('index')
        else:
            return render(request,'Post/edificadores.html',{"error":"Campos no validos"})


    else:
        datos = EdificadoresForm()
    
    
    return render(request,'Post/edificadores.html',{"datos":datos})



def detalle_casa_oracion(request,slug):
    oracion = get_object_or_404(CasaOracion,slug=slug)
    oracion2 = CasaOracion.objects.filter(status=True)
    if oracion:
        last = len(oracion2)-1
        last_prayer = oracion2[last]
    else:
        last_prayer=False


    return render(request,'Post/casa_oracion2.html',{'oracion':oracion,'last':last_prayer})


def blog(request):
    queryset = request.GET.get("buscar")
    post = PostBlog.objects.filter(status=True)
    last = len(post)-1
    last_post = post[last] 
    if queryset:
        post = PostBlog.objects.filter(
            Q(title__icontains=queryset) |
            Q(description__icontains=queryset)
        ).distinct()

    paginator = Paginator(post,1)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request,'Post/blog.html',{"posts":post,"last":last_post})


def detalle_Post(request,slug):
    post = get_object_or_404(PostBlog,slug=slug)
    post2 = PostBlog.objects.filter(status=True)
    last = len(post2)-1
    last_post = post2[last] 



    return render(request,'Post/blog2.html',{'posts':post,'last':last_post})