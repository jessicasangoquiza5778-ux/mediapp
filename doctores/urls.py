from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_doctores, name='lista_doctores'),
    path('crear/', views.crear_doctor, name='crear_doctor'),
    path('editar/<int:pk>/', views.editar_doctor, name='editar_doctor'),
    path('eliminar/<int:pk>/', views.eliminar_doctor, name='eliminar_doctor'),
]