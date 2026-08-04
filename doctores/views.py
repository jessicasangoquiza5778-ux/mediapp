from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor

def lista_doctores(request):
    doctores = Doctor.objects.all()
    return render(request, 'doctores/lista.html', {'doctores': doctores})

def crear_doctor(request):
    if request.method == 'POST':
        Doctor.objects.create(
            nombre_doctor=request.POST.get('nombre_doctor'),
            apellido_doctor=request.POST.get('apellido_doctor'),
            cedula_doctor=request.POST.get('cedula_doctor'),
            especialidad=request.POST.get('especialidad'),
            telefono_doctor=request.POST.get('telefono_doctor'),
            correo_doctor=request.POST.get('correo_doctor'),
            estado_doctor=request.POST.get('estado_doctor'),
        )
        return redirect('lista_doctores')
    return render(request, 'doctores/crear.html')

def editar_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.nombre_doctor = request.POST.get('nombre_doctor')
        doctor.apellido_doctor = request.POST.get('apellido_doctor')
        doctor.cedula_doctor = request.POST.get('cedula_doctor')
        doctor.especialidad = request.POST.get('especialidad')
        doctor.telefono_doctor = request.POST.get('telefono_doctor')
        doctor.correo_doctor = request.POST.get('correo_doctor')
        doctor.estado_doctor = request.POST.get('estado_doctor')
        doctor.save()
        return redirect('lista_doctores')
    return render(request, 'doctores/editar.html', {'doctor': doctor})

def eliminar_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('lista_doctores')
    return render(request, 'doctores/eliminar.html', {'doctor': doctor})