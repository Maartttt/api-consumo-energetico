from rest_framework import viewsets
from .models import Dispositivo, RegistroConsumo
from .serializers import DispositivoSerializer, RegistroConsumoSerializer

class DispositivoViewSet(viewsets.ModelViewSet):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer

class RegistroConsumoViewSet(viewsets.ModelViewSet):
    queryset = RegistroConsumo.objects.all()
    serializer_class = RegistroConsumoSerializer
