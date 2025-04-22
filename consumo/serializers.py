from rest_framework import serializers
from .models import Dispositivo, RegistroConsumo

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'

class RegistroConsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroConsumo
        fields = '__all__'


