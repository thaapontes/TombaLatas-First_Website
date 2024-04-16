from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('galeria.html', views.galeria),
    path('registro.html', views.registro, name='registro'),
    path('perfis/<int:perfil_id>', views.exibir),
    path('perfis/<int:perfil_id>/convidar', views.convidar, name='convidar'),
]