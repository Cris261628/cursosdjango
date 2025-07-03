from django.shortcuts import render

# Create your views here.
def encabezado(request):
    return render(request,"inicio/encabezado.html")

def principal(request):
    return render(request,"inicio/principal.html")

def cursos(request):
 return render(request,"inicio/cursos.html")

def contacto (request):
 return render(request,"inicio/contacto.html")


