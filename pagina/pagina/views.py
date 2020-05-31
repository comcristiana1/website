from django.http import HttpResponse


def prueba_error(request):
    return HttpResponse('Prueba Exitosa, momento de crear vistas att:Adrian Lima xD')