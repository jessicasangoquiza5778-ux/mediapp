from django.shortcuts import render, redirect, get_object_or_404
from .models import Cita
from .forms import CitaForm


def listar_citas(request):
    citas = Cita.objects.all()
    return render(request, 'citas/listar_citas.html', {'citas': citas})


def registrar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_citas')
    else:
        form = CitaForm()
    return render(request, 'citas/registrar_cita.html', {'form': form})


def editar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    form = CitaForm(request.POST or None, instance=cita)
    if form.is_valid():
        form.save()
        return redirect('listar_citas')
    return render(request, 'citas/editar_cita.html', {'form': form})


def eliminar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    cita.delete()
    return redirect('listar_citas')