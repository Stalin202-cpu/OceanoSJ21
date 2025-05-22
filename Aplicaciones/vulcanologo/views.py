from django.shortcuts import render, redirect
from .models import vulcanologo
from django.contrib import messages

def inicio(request):
    listadovulca = vulcanologo.objects.all()
    return render( request, "inicio.html", {'vulcanologo': listadovulca})


# Renderizar el formulario para nueva prueba
def nuevoVulca(request):
    return render(request, "nuevoVulca.html")

# Función encargada de guardar una nueva prueba en la base de datos
def guardarVulca(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    especialidad = request.POST["especialidad"]
    email = request.POST["email"]

    vulcanologo.objects.create(nombre=nombre, apellido=apellido, especialidad=especialidad, email=email )

    #Mensaje de confirmacion 
    messages.success(request, "Vulcanologo guardado exitosamente")
    return redirect('/')

# Eliminar una prueba por ID
def eliminarVulca(request, id):
    vulcaEliminar = vulcanologo.objects.get(id=id)
    vulcaEliminar.delete()
    return redirect('/')

# Mostrando formulario de ediccion
def editarVulca(request, id):
    vulcaEditar = vulcanologo.objects.get(id=id)
    return render(request, "editarVulca.html", {'vulcaEditar': vulcaEditar})

def procesarEdicionCajeros(request):
    
    id=request.POST["id"]
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    especialidad = request.POST["especialidad"]
    email = request.POST["email"]
    
    vulc2=vulcanologo.objects.get(id=id)
    vulc2.nombre=nombre
    vulc2.apellido=apellido
    vulc2.especialidad=especialidad
    vulc2.email=email
    vulc2.save()
    #Mensaje de confirmacion
    messages.success(request, "Vulcanologo Actualizado exitosamente")
    return redirect('/')