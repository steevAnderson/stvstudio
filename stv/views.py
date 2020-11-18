from django.shortcuts import render, HttpResponse

from stv.models import cliente, conocimiento, proyecto
# Create your views here.



def index(request):

    client = cliente.objects.all()
    
    proyect = proyecto.objects.all()
     
    return render(request, 'index.html', {
        'clientss' : client,
        'proyectos' : proyect

    })
    

def me(request):
    client = cliente.objects.all()
    conocimientos = conocimiento.objects.all()
    proyect = proyecto.objects.all()
    return render(request, 'me.html', {
        'conocimiento' : conocimientos,
        'clientss' : client,
        'proyectos' : proyect
    })

def contactar(request):
    return render(request, 'http://google.es')