from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_Pacientes, name='listar_Pacientes'),
    path('registrar_Pacientes/', views.registrar_Pacientes, name='registrar_Pacientes'),
    path('editar_Pacientes/<int:id>/', views.editar_Pacientes, name='editar_Pacientes'),
    path('eliminar_Pacientes/<int:id>/', views.eliminar_Pacientes, name='eliminar_Pacientes'),
]