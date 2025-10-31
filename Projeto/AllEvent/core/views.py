# Arquivo: core/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Evento # Importando o modelo Evento

# --- Views da Aplicação Principal ---

def home(request):
    return render(request, 'core/home.html') # Assumindo que home.html está em templates/core/

# --- Views de Autenticação e Usuário ---

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        nome = request.POST.get('nome_completo')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        senha_confirm = request.POST.get('password_confirm')

        if senha != senha_confirm:
            messages.error(request, 'As senhas não coincidem!')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está em uso.')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=email, email=email, password=senha)
        user.first_name = nome
        user.save()
        login(request, user)
        messages.success(request, 'Conta criada com sucesso!')
        return redirect('home')
    return render(request, 'core/cadastro.html') # Assumindo que cadastro.html está em templates/core/

@login_required
def perfil_view(request):
    return render(request, 'core/perfil.html') # Assumindo que perfil.html está em templates/core/

@login_required
def editar_dados(request):
    if request.method == 'POST':
        # Pega todos os dados do formulário
        senha_atual = request.POST.get('current_password')
        nome_completo = request.POST.get('name')
        email = request.POST.get('email')
        nova_senha = request.POST.get('password')

        # 1. VERIFICAÇÃO DE SEGURANÇA PRIMEIRO!
        # A função check_password compara a senha digitada com a senha criptografada no banco.
        if not request.user.check_password(senha_atual):
            messages.error(request, 'A senha atual está incorreta. Nenhuma alteração foi salva.')
            return redirect('editar_dados')

        # 2. SE A SENHA ESTIVER CORRETA, PROSSIGA COM AS ATUALIZAÇÕES
        
        # Atualiza o nome
        request.user.first_name = nome_completo

        # Atualiza o e-mail (com verificação de e-mail duplicado)
        if email and email != request.user.email:
            if User.objects.filter(email=email).exclude(pk=request.user.pk).exists():
                messages.error(request, 'Este e-mail já está sendo usado por outra conta.')
                return redirect('editar_dados')
            request.user.email = email
            request.user.username = email

        # Atualiza a senha APENAS se uma nova foi fornecida
        if nova_senha:
            request.user.set_password(nova_senha)

        # Salva as alterações no banco de dados
        request.user.save()

        messages.success(request, 'Seus dados foram atualizados com sucesso!')
        return redirect('editar_dados')
    
    return render(request, 'core/editar_dados.html')

@login_required
def favoritos_view(request):
    # Lógica a ser implementada no futuro
    return render(request, 'core/favoritos.html')

@login_required
def preferencias_view(request):
    # Lógica a ser implementada no futuro
    return render(request, 'core/preferencias.html')

# --- Views de Eventos ---

def lista_eventos(request):
    todos_os_eventos = Evento.objects.all()
    contexto = {'eventos': todos_os_eventos}
    return render(request, 'core/lista_eventos.html', contexto)

def buscar_eventos(request):
    return render(request, 'core/buscar_eventos.html')

def resultado_busca(request):
    termo = request.GET.get('termo_busca', '')
    if termo:
        eventos_filtrados = Evento.objects.filter(nome__icontains=termo)
    else:
        eventos_filtrados = []
    contexto = {'eventos': eventos_filtrados, 'termo_busca': termo}
    return render(request, 'core/lista_eventos.html', contexto)

def event_view(request):
    # Lógica para mostrar um evento específico (placeholder)
    return render(request, 'core/event.html')