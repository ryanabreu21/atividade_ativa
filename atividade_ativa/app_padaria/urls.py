
# app_padaria/urls.py
from django.urls import path
from . import views
from .views import lista_pedidos, detalhes_pedido, home

urlpatterns = [
    path('', home, name='home'),
    path('pedidos/', lista_pedidos, name='lista_pedidos'),
    path('pedidos/<int:pedido_id>/', detalhes_pedido, name='detalhes_pedido'),
    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reservas/<int:reserva_id>/', views.detalhes_reserva, name='detalhes_reserva'),
    path('fazer_pedido/', views.fazer_pedido, name='fazer_pedido'),
    path('fazer_reserva/', views.fazer_reserva, name='fazer_reserva'),
]

