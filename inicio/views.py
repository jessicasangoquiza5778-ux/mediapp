from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import authenticate, login, logout

def hola (request):
    return render(request,'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def servicios(request):
    return render(request, 'servicios.html')

def booking(request):
    return render(request, 'booking.html')

def tecnicos(request):
    return render(request, 'tecnicos.html')

def testimonio(request):
    return render(request, 'testimonio.html')

def login_view(request):
    mensaje=''
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect ('dashboard')
        else:
            mensaje='Usuario o contraseña incorrectos'
    return render(request,'login.html',{'mensaje':mensaje})

def dashboard(request):
    return render(request, 'private/dashboard.html') # ← agrega dashboard/


def recuperar(request):
    return render(request, 'recuperar.html')

def servicio(request):
    return render(request, 'private/servicio.html')

def logout_view(request):
    logout(request)
    return redirect('login')