from django.shortcuts import render
def home(request):
    return render(request, 'MeuSite/home.html')
def cadastro(request):
    return render(request, 'MeuSite/cadastro.html')
def login_view(request):
    return render(request, 'MeuSite/login.html')
def editar_dados_view(request):
    return render(request, 'MeuSite/editar-dados.html')
def favoritos_view(request):
    return render(request, 'MeuSitefavoritos.html')
def perfil_view(request):
    return render(request, 'MeuSite/perfil.html')
def preferencias_view(request):
    return render(request, 'MeuSite/preferencias.html')
def lista_view(request):
    return render(request, 'MeuSite/lista.html')
def event_view(request):
    return render(request, 'MeuSite/event.html')