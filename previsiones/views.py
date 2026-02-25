import random
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Plato, PrevisionDiaria
from .forms import PlatoForm, PrevisionForm

def lista_platos(request):
    platos = Plato.objects.all()
    previsiones = PrevisionDiaria.objects.all()
    
    if request.method == 'POST':
        form = PlatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_platos')
    else:
        form = PlatoForm()

    return render(request, 'previsiones/lista_platos.html', {
        'platos': platos, 
        'previsiones': previsiones,
        'form': form
    })

def borrar_plato(request, plato_id):
    plato = get_object_or_404(Plato, id=plato_id)
    if request.method == 'POST':
        plato.delete()
        return redirect('lista_platos')
    return render(request, 'previsiones/borrar_plato.html', {'plato': plato})

def editar_plato(request, plato_id):
    plato = get_object_or_404(Plato, id=plato_id)
    if request.method == 'POST':
        form = PlatoForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect('lista_platos')
    else:
        form = PlatoForm(instance=plato)
    
    return render(request, 'previsiones/editar_plato.html', {'form': form, 'plato': plato})

def crear_prevision(request):
    if request.method == 'POST':
        form = PrevisionForm(request.POST)
        if form.is_valid():
            prevision = form.save(commit=False)
            
            base_ventas = 20
            fecha_dt = datetime.combine(prevision.fecha, datetime.min.time())
            dia_semana = fecha_dt.weekday()
            
            multiplicador = 1.0
            if dia_semana >= 4:
                multiplicador = 1.8
            
            festivos_simulados = [1, 5, 12, 25]
            if prevision.fecha.day in festivos_simulados:
                multiplicador += 0.5
                
            prevision.cantidad_estimada = int(base_ventas * multiplicador + random.randint(1, 10))
            prevision.save()
            return redirect('lista_platos')
    else:
        form = PrevisionForm()
    
    return render(request, 'previsiones/crear_prevision.html', {'form': form})