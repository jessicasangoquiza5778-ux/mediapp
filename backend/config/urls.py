from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctores/', views.doctor_list, name='doctor_list'),
    path('doctores/crear/', views.doctor_create, name='doctor_create'),
    path('doctores/editar/<int:pk>/', views.doctor_update, name='doctor_update'),
    path('doctores/borrar/<int:pk>/', views.doctor_delete, name='doctor_delete'),
    
    # ESTA ES LA LÍNEA QUE VA A CARGAR TU PÁGINA DE INICIO (EL INDEX.HTML DE CLINIC)
    path('', views.clinic_home, name='clinic_home'),
]