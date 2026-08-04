import django.urls
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    django.urls.path('login/', TokenObtainPairView.as_view(), name ='token_ontain_pair'),
    django.urls.path('refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
]