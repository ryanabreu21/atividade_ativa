# padaria/forms.py
from django import forms
from .models import Pedido, Reserva

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nome_cliente', 'itens_pedido']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nome_cliente', 'quantidade_pessoas', 'data_reserva']
        widgets = {
        'data_reserva': forms.DateInput(attrs={'type': 'date'}),
    }
