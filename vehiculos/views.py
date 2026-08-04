from django.contrib import messages
from django.shortcuts import redirect, render
from vehiculos.models import Vehiculo

# Create your views here.
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, "vehiculos/listar_vehiculos.html", {'vehiculos': vehiculos})

def crear_vehiculos(request):
    if request.method == "POST":
        placa_vehiculo = request.POST.get("placaVehiculo")
        marca_vehiculo = request.POST.get("marcaVehiculo")
        modelo_vehiculo = request.POST.get("modeloVehiculo")
        anio_vehiculo = request.POST.get("anioVehiculo")
        color_vehiculo = request.POST.get("colorVehiculo")
        tipo_vehiculo = request.POST.get("tipoVehiculo")
        estado_vehiculo = request.POST.get("estadoVehiculo")

        Vehiculo.objects.create(
            placa_vehiculo = placa_vehiculo,
            marca_vehiculo = marca_vehiculo,
            modelo_vehiculo = modelo_vehiculo,
            anio_vehiculo = anio_vehiculo,
            color_vehiculo = color_vehiculo,
            tipo_vehiculo = tipo_vehiculo,
            estado_vehiculo = estado_vehiculo
        )
        messages.success(request, "Vehículo agregado con éxito")
        return redirect('listar_vehiculos')
    return render(request, 'vehiculos/crear_vehiculos.html')

def eliminar_vehiculos(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    vehiculo.delete()
    messages.success(request, "Vehículo eliminado")
    return redirect("listar_vehiculos")

def editar_vehiculos(request, id):
    vehiculo = Vehiculo.objects.get(id=id)

    if request.method == "POST":
        vehiculo.placa_vehiculo = request.POST.get("placaVehiculoEdit")
        vehiculo.marca_vehiculo = request.POST.get("marcaVehiculoEdit")
        vehiculo.modelo_vehiculo = request.POST.get("modeloVehiculoEdit")
        vehiculo.anio_vehiculo = request.POST.get("anioVehiculoEdit")
        vehiculo.color_vehiculo = request.POST.get("colorVehiculoEdit")
        vehiculo.tipo_vehiculo = request.POST.get("tipoVehiculoEdit")
        vehiculo.estado_vehiculo = request.POST.get("estadoVehiculoEdit")

        vehiculo.save()
        messages.success(request, "Vehículo actualizado")
        return redirect("listar_vehiculos")
    return render(request, "vehiculos/editar_vehiculo.html", {"vehiculo": vehiculo})