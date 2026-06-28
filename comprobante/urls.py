from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_comprobantes, name='lista_comprobantes'),
    path('crear/', views.crear_comprobante, name='crear_comprobante'),
    path('editar/<int:pk>/', views.editar_comprobante, name='editar_comprobante'),
    path('eliminar/<int:pk>/', views.eliminar_comprobante, name='eliminar_comprobante'),
]
