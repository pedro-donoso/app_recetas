from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Receta

def inicio(request):
    recetas = Receta.objects.all()[:3]
    return render(request, 'recetas/inicio.html', {'recetas': recetas})

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas/lista_recetas.html', {'recetas': recetas})

def detalle_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'recetas/detalle_receta.html', {'receta': receta})

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        
        if not all([nombre, email, mensaje]):
            messages.warning(request, 'Por favor, completa todos los campos.')
            return render(request, 'recetas/contacto.html')
        
        return redirect('recetas:contacto_exito')
    
    return render(request, 'recetas/contacto.html')

def contacto_exito(request):
    return render(request, 'recetas/contacto_exito.html')