from django.shortcuts import render,redirect
from .models import Miembro,CasaOracion,Oracion,O_P,Activities,Ministry
from .forms import O_PForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.




def mostrar_pastor(request):
    mostrar = Miembro.objects.all()
    return render(request,'index.html',{'mostrar':mostrar})

def casa_oracion(request):
    oracion = CasaOracion.objects.all()
    return render(request,'casa_oracion.html',{'oracion':oracion})

def oracion(request):
    oracion = Oracion.objects.all()
    return render(request,'oracion.html',{'oracion':oracion})


def mostrar_actividades(request):
    actividad = Activities.objects.all()
    return render(request,'actividades.html',{'actividad':actividad})

def mostrar_ministerio(request):
    ministerio = Ministry.objects.all()
    return render(request,'ministerios.html',{'ministerio':ministerio})    


def oracion_peticion(request):

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

    return render(request,'prueba.html',{'datos':O_P_form})


