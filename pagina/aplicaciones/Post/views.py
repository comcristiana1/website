from django.shortcuts import render
from .models import Miembro
# Create your views here.


def mostrar_pastor(request):
    mostrar = Miembro.objects.all()
    return render(request,'index.html',{'mostrar':mostrar})









