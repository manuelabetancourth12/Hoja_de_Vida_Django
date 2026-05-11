from django.contrib import admin
from django.urls import path
from cv_manuela import views # Importamos tus vistas de ingeniería

urlpatterns = [
    path('admin/', admin.site.urls), # Corregido: es .urls, no .core
    path('', views.home, name='home'), # Tu página principal
]