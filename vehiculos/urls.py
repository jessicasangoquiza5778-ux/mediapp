from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_vehiculos, name='listar_vehiculos'),
    path('crear_vehiculo/', views.crear_vehiculos, name='crear_vehiculos'),
    path('editar_vehiculos/<int:id>/', views.editar_vehiculos, name='editar_vehiculos'),
    path('eliminar_vehiculos/<int:id>/', views.eliminar_vehiculos, name='eliminar_vehiculos'),
]