from django.shortcuts import render
from django.http import HttpResponse
from gestionCalificaciones.models import Califas

# Create your views here.


def busqueda(request):
    return render(request, 'busqueda.html')


def consulta(request):
    return render(request, 'consulta.html')


def ingreso(request):
    return render(request, 'ingreso.html')


def nuevo_ingreso(request):
    data = Califas(materia=request.GET["materia"], alumno=request.GET["alumno"],
                   cal1=request.GET["cal1"], cal2=request.GET["cal2"], cal3=request.GET["cal3"])
    data.save()
    return HttpResponse("registro exitoso! Materia: %s | Alumno: %s | cal 1: %s | cal 2: %s | cal 3: %s" % (request.GET["materia"], request.GET["alumno"], request.GET["cal1"], request.GET["cal2"], request.GET["cal3"]))


def buscar_calificacion_materia(request):

    if request.GET["materia"]:

        producto = request.GET["materia"]
        califas = Califas.objects.filter(materia__icontains=producto)
        for califa in califas:
            califa.prom = (califa.cal1 + califa.cal2 + califa.cal3)/3
        return render(request, "consulta.html", {"califas": califas, "query": producto})

    else:
        mensaje = "no has ingresado el nombre de la materia"

    return HttpResponse(mensaje)


def buscar_calificacion_alumno(request):

    if request.GET["alumno"]:

        producto = request.GET["alumno"]
        califas = Califas.objects.filter(alumno__icontains=producto)
        for califa in califas:
            califa.prom = (califa.cal1 + califa.cal2 + califa.cal3)/3
        return render(request, "consulta.html", {"califas": califas, "query": producto})

    else:
        mensaje = "no has ingresado un nombre de alumno"

    return HttpResponse(mensaje)
