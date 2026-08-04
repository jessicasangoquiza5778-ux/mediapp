from django.contrib import messages
from django.shortcuts import redirect, render

from clientes.models import Pacientes


def listar_Pacientes(request):
    pacientes = Pacientes.objects.all()
    return render(request, "clientes/listar_clientes.html", {'Pacientes': pacientes})


def registrar_Pacientes(request):
    if request.method == "POST":
        nombre_Pacientes = request.POST.get("nombrePacientes")
        apellido_Pacientes = request.POST.get("apellidoPacientes")
        cedula_Pacientes = request.POST.get("cedulaPacientes")
        telefono_Pacientes = request.POST.get("telefonoPacientes")
        direccion_Pacientes = request.POST.get("direccionPacientes")
        estado_Pacientes = request.POST.get("estadoPacientes")

        Pacientes.objects.create(
            nombre_Pacientes=nombre_Pacientes,
            apellido_Pacientes=apellido_Pacientes,
            cedula_Pacientes=cedula_Pacientes,
            telefono_Pacientes=telefono_Pacientes,
            direccion_Pacientes=direccion_Pacientes,
            estado_Pacientes=estado_Pacientes
        )

        messages.success(request, "Paciente agregado con éxito")
        return redirect('listar_Pacientes')

    return render(request, 'clientes/registrar_clientes.html')


def eliminar_Pacientes(request, id):
    paciente = Pacientes.objects.get(id=id)
    paciente.delete()

    messages.success(request, "Paciente eliminado")
    return redirect("listar_Pacientes")


def editar_Pacientes(request, id):
    paciente = Pacientes.objects.get(id=id)

    if request.method == "POST":
        paciente.nombre_Pacientes = request.POST.get("nombrePacientesEdit")
        paciente.apellido_Pacientes = request.POST.get("apellidoPacientesEdit")
        paciente.cedula_Pacientes = request.POST.get("cedulaPacientesEdit")
        paciente.telefono_Pacientes = request.POST.get("telefonoPacientesEdit")
        paciente.direccion_Pacientes = request.POST.get("direccionPacientesEdit")
        paciente.estado_Pacientes = request.POST.get("estadoPacientesEdit")

        paciente.save()

        messages.success(request, "Paciente actualizado")
        return redirect("listar_Pacientes")

    return render(
        request,
        "clientes/editar_clientes.html",
        {"Pacientes": paciente}
    )