from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$','perfis.views.index', name='index'),
    url(r'^galeria.html$', 'perfis.views.galeria'),
    url(r'^registro.html$', 'perfis.views.registro', name='registro'),
    url(r'^perfis/(?P<perfil_id>\d+)$', 'perfis.views.exibir'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', 'perfis.views.convidar', name='convidar')
)