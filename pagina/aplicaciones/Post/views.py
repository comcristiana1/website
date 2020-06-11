from django.shortcuts import render
from .models import Miembro,CasaOracion,Oracion,Activities,Ministry
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






