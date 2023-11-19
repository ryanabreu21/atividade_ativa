

# padaria/models.py
from django.db import models
from django.utils import timezone

class Pedido(models.Model):
    nome_cliente = models.CharField(max_length=255)
    itens_pedido = models.TextField()
    data_hora_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.nome_cliente} em {self.data_hora_pedido}"

class Reserva(models.Model):
    nome_cliente = models.CharField(max_length=255)
    quantidade_pessoas = models.IntegerField()
    data_reserva = models.DateField()

    def __str__(self):
        # Formata a data no formato desejado (d/m/Y)
        data_formatada = self.data_reserva.strftime("%d/%m/%Y")
        return f"{self.nome_cliente} - {data_formatada}"
