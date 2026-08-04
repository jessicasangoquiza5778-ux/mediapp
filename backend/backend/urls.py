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

# Vista de inicio
def home(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>MediApp API</title>
        <style>
            body { font-family: Arial; margin: 40px; background: #f0f2f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
            h1 { color: #2c3e50; }
            .endpoint { background: #ecf0f1; padding: 10px; margin: 10px 0; border-radius: 5px; }
            .endpoint a { color: #3498db; text-decoration: none; }
            .endpoint a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🏥 MediApp API</h1>
            <p>Sistema de gestión médica - API REST</p>
            
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
    path('', home, name='home'),  # 👈 Agrega esta línea
    path('admin/', admin.site.urls),
    path('api/', include('usuarios.urls')),
    path('api/', include('categories.urls')),  
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]