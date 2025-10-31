"""
URL configuration for AllEvent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from AllEvent import views  # Import the home view
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),

    path('cadastro_site/', views.cadastro, name='cadastro'),
    path('editar-dados/', views.editar_dados_view, name='editar_dados'),
    path('favoritos/', views.favoritos_view, name='favoritos'),
    path('perfil_site/', views.perfil_view, name='perfil'),
    path('preferencias/', views.preferencias_view, name='preferencias'),
    path('lista/', views.lista_view, name='lista'),
    path('home_site/', views.home, name='home'),
    path('event_site/', views.event_view, name='event'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
]