

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_padaria/', include('app_padaria.urls')),  
    path('', include('app_padaria.urls')),  # Isso redireciona a rota raiz para o app_padaria
]


