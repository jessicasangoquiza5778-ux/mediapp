from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from .models import OrdenTrabajo

def dashboard(request):
    return render(request, 'private/dashboard.html')

def informe(request):
    return render(request, 'private/informe.html')

def listar_usuarios(request):
    usuarios = User.objects.all()
    contexto = {'usuarios': usuarios}
    return render(request, 'private/listar_usuarios.html', contexto)

def iconos(request):
    return render(request, 'private/iconos.html')

def crear_usuarios(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
            return render(request, "private/crear_usuarios.html")
        if User.objects.filter(email=email).exists():
            messages.error(request, "El email ya existe")
            return render(request, "private/crear_usuarios.html")
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Usuario creado con éxito")
        return redirect('listar_usuarios')
    return render(request, "private/crear_usuarios.html")

def eliminar_usuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    messages.success(request, "Usuario eliminado")
    return redirect("listar_usuarios")

def editar_usuario(request, id):
    usuario = User.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST.get("username_edit")
        email = request.POST.get("email_edit")
        password = request.POST.get("password_edit")
        if User.objects.filter(username=username).exclude(id=id).exists():
            messages.error(request, "El usuario ya esta registrado")
            return render(request, "private/editar_usuario.html", {"usuario": usuario})
        if User.objects.filter(email=email).exclude(id=id).exists():
            messages.error(request, "El email ya existe")
            return render(request, "private/editar_usuario.html", {"usuario": usuario})
        usuario.username = username
        usuario.email = email
        if password:
            usuario.set_password(password)
        usuario.save()
        messages.success(request, "El registro se ha actualizado correctamente")
        return redirect("listar_usuarios")
    return render(request, "private/editar_usuario.html", {"usuario": usuario})

def orden_trabajo(request):
    ordenes = OrdenTrabajo.objects.all().order_by('-fecha_creacion')
    return render(request, 'private/orden_trabajo.html', {'ordenes': ordenes})

def nueva_orden(request):
    if request.method == 'POST':
        OrdenTrabajo.objects.create(
            numero_orden=request.POST.get('numero_orden'),
            nombre=request.POST.get('nombre'),
            fecha=request.POST.get('fecha'),
            tipo_vehiculo=request.POST.get('tipo_vehiculo'),
            marca=request.POST.get('marca'),
            placas=request.POST.get('placas'),
            telefono=request.POST.get('telefono'),
            estado=request.POST.get('estado', 'pendiente'),
            otros=request.POST.get('otros', ''),
        )
        messages.success(request, "Orden creada con éxito")
        return redirect('orden_trabajo')
    return render(request, 'private/guardar_orden_trabajo.html')

def editar_orden(request, id):
    orden = get_object_or_404(OrdenTrabajo, id=id)
    if request.method == 'POST':
        orden.numero_orden = request.POST.get('numero_orden')
        orden.nombre = request.POST.get('nombre')
        orden.fecha = request.POST.get('fecha')
        orden.tipo_vehiculo = request.POST.get('tipo_vehiculo')
        orden.marca = request.POST.get('marca')
        orden.placas = request.POST.get('placas')
        orden.telefono = request.POST.get('telefono')
        orden.total = request.POST.get('total') or 0
        orden.estado = request.POST.get('estado', 'pendiente')
        orden.otros = request.POST.get('otros', '')
        orden.save()
        messages.success(request, "Orden actualizada con éxito")
        return redirect('orden_trabajo')
    return render(request, 'private/editar_orden.html', {'orden': orden})

def eliminar_orden(request, id):
    orden = get_object_or_404(OrdenTrabajo, id=id)
    orden.delete()
    messages.success(request, "Orden eliminada")
    return redirect('orden_trabajo')

def ver_orden(request, id):
    orden = get_object_or_404(OrdenTrabajo, id=id)
    return render(request, 'private/ver_orden.html', {'orden': orden})

def comprobante_servicio(request):
    contexto = {
        'titulo': 'Comprobante de Servicio',
    }
    return render(request, 'private/comprobante_servicio.html', contexto)

def guardar_comprobante(request):
    if request.method == 'POST':
        messages.success(request, "Comprobante generado con éxito")
        return redirect('comprobante_servicio')
    return redirect('comprobante_servicio')

def logout_view(request):
    logout(request)
    return redirect('login')  # 'login' debe ser el name= definido en inicio/urls.py