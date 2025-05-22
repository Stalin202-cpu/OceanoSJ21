from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('nuevoVulca', views.nuevoVulca),  # corregido
    path('guardarVulca', views.guardarVulca),  # corregido
    path('eliminarVulca/<id>', views.eliminarVulca),  # corregido
    path('editarVulca/<id>',views.editarVulca),
    path('procesarEdicionVulca', views.procesarEdicionVulca)
]