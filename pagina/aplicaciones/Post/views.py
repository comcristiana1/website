from django.shortcuts import render,redirect
from .models import CasaOracion,Ministry,Evento,Groups,Recurso
from .models import Actividades
from .models import Miembro
from .forms import O_PForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator
# Create your views here.



def home(request):
    return render(request,'base.html')



def mostrar_pastor(request):
    mostrar = Miembro.objects.all()
    return render(request,'Post/quienessomos.html',{'mostrar':mostrar})

def casa_oracion(request):
    oracion = CasaOracion.objects.all()
    last = len(oracion)-1
    last_prayer = oracion[last] 
    paginator = Paginator(oracion,1)
    page = request.GET.get('page')
    oracion = paginator.get_page(page)
    return render(request,'Post/casa_oracion.html',{'oracion':oracion,'last':last_prayer})





def mostrar_actividades(request):
    actividad = Actividades.objects.all()
    return render(request,'Post/actividades.html',{'actividad':actividad})

def mostrar_ministerio(request):
    ministerio = Ministry.objects.all()
    return render(request,'POST/ministerios.html',{'ministerio':ministerio})    


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
            return redirect('Post:orar')
    else:
        O_P_form = O_PForm()

    return render(request,'Post/recursos.html',{'datos':O_P_form,'recursos':libros})


def mostrar_eventos(request):
    eventos = Evento.objects.all()
    return render(request,'POST/eventos.html',{'eventos':eventos})

def mostrar_eventosEspirituales(request):
    eventos = Evento.objects.all().filter(category = 'Espirituales');
    return render(request,'POST/eventos.html',{'eventos':eventos})    

def mostrar_eventosSociales(request):
    eventos = Evento.objects.all().filter(category = 'Sociales');
    return render(request,'POST/eventos.html',{'eventos':eventos})

def mostrar_grupos(request):
    grupos = Groups.objects.all()
    return render(request,'POST/grupos.html',{'grupos':grupos})