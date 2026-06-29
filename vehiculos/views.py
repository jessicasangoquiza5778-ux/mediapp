from django.contrib import messages
from django.shortcuts import redirect, render
from vehiculos.models import Vehiculo

# Create your views here.
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, "vehiculos/listar_vehiculos.html", {'vehiculos': vehiculos})

def crear_vehiculos(request):
    if request.method == "POST":
        nombre_vehiculo = request.POST.get("nombreVehiculo")
        precio_vehiculo = request.POST.get("precioVehiculo")
        stock_vehiculo = request.POST.get("stockVehiculo")
        estado_vehiculo = request.POST.get("estadoVehiculo")

        Vehiculo.objects.create(
            nombre_vehiculo = nombre_vehiculo,
            precio_vehiculo = precio_vehiculo,
            stock_vehiculo = stock_vehiculo,
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
        vehiculo.nombre_vehiculo = request.POST.get("nombreVehiculoEdit")
        vehiculo.precio_vehiculo = request.POST.get("precioVehiculoEdit")
        vehiculo.stock_vehiculo = request.POST.get("stockVehiculoEdit")
        vehiculo.estado_vehiculo = request.POST.get("estadoVehiculoEdit")

        vehiculo.save()
        messages.success(request, "Vehículo actualizado")
        return redirect("listar_vehiculos")
    return render(request, "vehiculos/editar_vehiculo.html", {"vehiculo": vehiculo})