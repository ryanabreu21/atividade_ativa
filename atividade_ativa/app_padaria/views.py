

# Create your views here.
# padaria/views.py
# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido, Reserva
from .forms import PedidoForm, ReservaForm
from django.utils.dateparse import parse_datetime


def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'app_padaria/lista_pedidos.html', {'pedidos': pedidos})

def detalhes_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    return render(request, 'app_padaria/detalhes_pedido.html', {'pedido': pedido})

def fazer_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'app_padaria/fazer_pedido.html', {'form': form})


def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'app_padaria/lista_reservas.html', {'reservas': reservas})

def detalhes_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    return render(request, 'app_padaria/detalhes_reserva.html', {'reserva': reserva})

def fazer_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm()
    return render(request, 'app_padaria/fazer_reserva.html', {'form': form})

def home(request):
    return render(request, 'app_padaria/home.html')
