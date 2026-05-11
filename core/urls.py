from django.contrib import admin
from django.urls import path
from cv_manuela import views # Importamos tus vistas

urlpatterns = [
    path('admin/', admin.site.urls), # Aquí estaba el error, ya corregido
    path('', views.home, name='home'),
]