from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DispositivoViewSet, RegistroConsumoViewSet

router = DefaultRouter()
router.register(r'dispositivos', DispositivoViewSet)
router.register(r'registros', RegistroConsumoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
