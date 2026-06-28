from django.shortcuts import render, get_object_or_404, redirect
from .models import ComprobanteServicio

def lista_comprobantes(request):
    comprobantes = ComprobanteServicio.objects.all()
    return render(request, 'comprobante/lista.html', {'comprobantes': comprobantes})

def crear_comprobante(request):
    if request.method == 'POST':
        numero_comprobante = request.POST['numero_comprobante']
        fecha = request.POST['fecha']
        cliente = request.POST['cliente']
        descripcion = request.POST['descripcion']
        total = request.POST['total']
        ComprobanteServicio.objects.create(
            numero_comprobante=numero_comprobante,
            fecha=fecha,
            cliente=cliente,
            descripcion=descripcion,
            total=total
        )
        return redirect('lista_comprobantes')
    return render(request, 'comprobante/crear.html')

def editar_comprobante(request, pk):
    comprobante = get_object_or_404(ComprobanteServicio, pk=pk)
    if request.method == 'POST':
        comprobante.numero_comprobante = request.POST['numero_comprobante']
        comprobante.fecha = request.POST['fecha']
        comprobante.cliente = request.POST['cliente']
        comprobante.descripcion = request.POST['descripcion']
        comprobante.total = request.POST['total']
        comprobante.save()
        return redirect('lista_comprobantes')
    return render(request, 'comprobante/editar.html', {'comprobante': comprobante})

def eliminar_comprobante(request, pk):
    comprobante = get_object_or_404(ComprobanteServicio, pk=pk)
    if request.method == 'POST':
        comprobante.delete()
        return redirect('lista_comprobantes')
    return render(request, 'comprobante/eliminar.html', {'comprobante': comprobante})