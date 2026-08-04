from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from categories.models import Categoria  # 👈 Importa el modelo

# Vista de inicio con datos reales
def home(request):
    # Obtener categorías de la base de datos
    categorias = Categoria.objects.all()
    
    # Generar HTML con las categorías
    html_categorias = ""
    if categorias:
        for cat in categorias:
            html_categorias += f"<li>📂 <strong>{cat.nombre}</strong> - {cat.descripcion or 'Sin descripción'}</li>"
    else:
        html_categorias = "<li>⚠️ No hay categorías aún. <a href='/admin/categories/categoria/add/'>Crea una desde el admin</a></li>"
    
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>MediApp API</title>
        <style>
            body {{ font-family: Arial; margin: 40px; background: #f0f2f5; }}
            .container {{ max-width: 1000px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #2c3e50; }}
            h2 {{ color: #34495e; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
            .endpoint {{ background: #ecf0f1; padding: 10px; margin: 10px 0; border-radius: 5px; }}
            .endpoint a {{ color: #3498db; text-decoration: none; }}
            .endpoint a:hover {{ text-decoration: underline; }}
            .categorias {{ background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0; }}
            .categorias li {{ padding: 8px; border-bottom: 1px solid #ddd; list-style: none; }}
            .categorias li:last-child {{ border-bottom: none; }}
            .stats {{ display: flex; gap: 20px; margin: 20px 0; }}
            .stat-box {{ background: #3498db; color: white; padding: 15px; border-radius: 5px; flex: 1; text-align: center; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🏥 MediApp</h1>
            <p>Sistema de gestión médica - API REST</p>
            
            <div class="stats">
                <div class="stat-box">
                    <h3>{categorias.count()}</h3>
                    <p>Categorías</p>
                </div>
                <div class="stat-box">
                    <h3>0</h3>
                    <p>Productos</p>
                </div>
                <div class="stat-box">
                    <h3>0</h3>
                    <p>Usuarios</p>
                </div>
            </div>
            
            <h2>📂 Categorías registradas</h2>
            <div class="categorias">
                <ul>
                    {html_categorias}
                </ul>
            </div>
            
            <h2>📌 Endpoints disponibles:</h2>
            
            <div class="endpoint">
                <strong>📊 Admin:</strong> <a href="/admin/">/admin/</a>
            </div>
            
            <div class="endpoint">
                <strong>👤 Usuarios:</strong> <a href="/api/">/api/</a>
            </div>
            
            <div class="endpoint">
                <strong>🔐 Token JWT:</strong> <a href="/api/token/">/api/token/</a>
            </div>
            
            <div class="endpoint">
                <strong>🔄 Refresh Token:</strong> <a href="/api/token/refresh/">/api/token/refresh/</a>
            </div>
            
            <div class="endpoint">
                <strong>📚 Documentación Swagger:</strong> <a href="/api/docs/">/api/docs/</a>
            </div>
            
            <div class="endpoint">
                <strong>📖 Documentación ReDoc:</strong> <a href="/api/redoc/">/api/redoc/</a>
            </div>
            
            <div class="endpoint">
                <strong>📋 Esquema API:</strong> <a href="/api/schema/">/api/schema/</a>
            </div>
        </div>
    </body>
    </html>
    """)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('usuarios.urls')),
    path('api/', include('categories.urls')),  
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]