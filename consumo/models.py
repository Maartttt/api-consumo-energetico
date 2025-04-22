from django.db import models

from django.db import models

class Dispositivo(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome

class RegistroConsumo(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name='registros')
    data = models.DateField()
    consumo_kwh = models.FloatField()

    def __str__(self):
        return f"{self.dispositivo.nome} - {self.data}"

