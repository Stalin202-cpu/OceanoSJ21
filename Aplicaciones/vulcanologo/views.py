from django.shortcuts import render, redirect
from .models import vulcanologo

def inicio(request):
    listadoCajeros = vulcanologo.objects.all()
    return render( request, "inicio.html", {'Cajeros': listadoCajeros})
