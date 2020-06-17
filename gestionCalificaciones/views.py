from django.shortcuts import render

# Create your views here.


def registro(request):
    return render(request, 'registro.html')

def consulta(request):
    return render(request, 'consulta.html')
