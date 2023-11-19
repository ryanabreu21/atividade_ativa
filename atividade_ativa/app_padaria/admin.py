from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pedido, Reserva

admin.site.register(Pedido)
admin.site.register(Reserva)