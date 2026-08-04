from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctores/', views.doctor_list, name='doctor_list'),
    path('doctores/crear/', views.doctor_create, name='doctor_create'),
    path('doctores/editar/<int:pk>/', views.doctor_update, name='doctor_update'),
    path('doctores/borrar/<int:pk>/', views.doctor_delete, name='doctor_delete'),
    
    # PÁGINA DE INICIO
    path('', views.clinic_home, name='clinic_home'),

    # NUEVAS PÁGINAS DE LA PLANTILLA
    path('about/', views.about, name='about'),
    path('departments/', views.departments, name='departments'),
    path('services/', views.services, name='services'),
    path('doctors/', views.doctors_page, name='doctors_page'),
    path('contact/', views.contact, name='contact'),
    path('appointment/', views.appointment, name='appointment'),
]