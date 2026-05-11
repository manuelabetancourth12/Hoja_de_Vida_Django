from django.contrib import admin
from django.urls import path
from cv_manuela import views # Importamos tus vistas

urlpatterns = [
    path('admin/', admin.site.core),
    path('', views.home, name='home'), # Esta línea hace que tu CV sea la página principal
]