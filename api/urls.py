from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import JuegoViewSet, JuegoAdminViewSet

from . import views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)

router = DefaultRouter()
router.register(r'juegos',JuegoViewSet, basename='juegos'),
router.register(r'admin/juegos',JuegoAdminViewSet, basename='admin-juegos'),
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    
    
    # jwt
    path("token/",TokenObtainPairView.as_view(),name="token_obtain_pain"),
    path("token/refresh",TokenRefreshView.as_view(),name="token_refresh"),
    # swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
]
