from django.shortcuts import render
from .models import Categoria
from .serializers import CategoriaSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(description='Lista todas las categorías', tags=['Categorías']),
    create=extend_schema(description='Crea una nueva categoría', tags=['Categorías']),
    retrieve=extend_schema(description='Obtiene una categoría por ID', tags=['Categorías']),
    update=extend_schema(description='Actualiza una categoría', tags=['Categorías']),
    partial_update=extend_schema(description='Actualización parcial de categoría', tags=['Categorías']),
    destroy=extend_schema(description='Elimina una categoría', tags=['Categorías']),
)
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('-id')
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]