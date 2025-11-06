# Arquivo: AllEvent/AllEvent/urls.py

from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', views.home, name='home'), 

    path('cadastro/', views.cadastro, name='cadastro'),

    path('perfil/', views.perfil_view, name='perfil'),
    path('perfil/editar/', views.editar_dados, name='editar_dados'),
    path('perfil/favoritos/', views.favoritos_view, name='favoritos'),
    path('perfil/preferencias/', views.preferencias_view, name='preferencias'),

    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/buscar/', views.buscar_eventos, name='buscar_eventos'),
    path('eventos/resultado/', views.resultado_busca, name='resultado_busca'),
    path('evento/<int:evento_id>/', views.detalhe_evento, name='detalhe_evento'),
    path('evento/detalhe/', views.event_view, name='event'),
]