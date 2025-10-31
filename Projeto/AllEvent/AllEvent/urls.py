# Arquivo: AllEvent/AllEvent/urls.py

from django.contrib import admin
from django.urls import path, include
from core import views  # Importando as views do nosso app 'core'

urlpatterns = [
    # URLs do Admin e de Autenticação (Login/Logout)
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # URL da Página Inicial
    # O caminho '' significa a raiz do site (ex: http://localhost:8000/)
    path('', views.home, name='home'), 

    # URL para a página de Cadastro
    path('cadastro/', views.cadastro, name='cadastro'),

    # URLs relacionadas ao Perfil do Usuário (agora organizadas)
    path('perfil/', views.perfil_view, name='perfil'),
    path('perfil/editar/', views.editar_dados, name='editar_dados'),
    path('perfil/favoritos/', views.favoritos_view, name='favoritos'),
    path('perfil/preferencias/', views.preferencias_view, name='preferencias'),

    # URLs de Consulta de Eventos
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/buscar/', views.buscar_eventos, name='buscar_eventos'),
    path('eventos/resultado/', views.resultado_busca, name='resultado_busca'),
    
    # URL de placeholder para a página de um evento específico
    path('evento/detalhe/', views.event_view, name='event'),
]