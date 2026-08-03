from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor

# Página de inicio de la plantilla Clinic
def clinic_home(request):
    return render(request, 'index.html')

# CRUD de Doctores

# 1. LEER (Listar doctores)
def doctor_list(request):
    doctores = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctores': doctores})

# 2. CREAR (Agregar nuevo doctor)
def doctor_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        specialty = request.POST.get('specialty')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        Doctor.objects.create(name=name, specialty=specialty, phone=phone, email=email)
        return redirect('doctor_list')
    return render(request, 'doctors/doctor_form.html')

# 3. EDITAR (Actualizar datos)
def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.name = request.POST.get('name')
        doctor.specialty = request.POST.get('specialty')
        doctor.phone = request.POST.get('phone')
        doctor.email = request.POST.get('email')
        doctor.save()
        return redirect('doctor_list')
    return render(request, 'doctors/doctor_form.html', {'doctor': doctor})

# 4. BORRAR (Eliminar)
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctors/doctor_confirm_delete.html', {'doctor': doctor})