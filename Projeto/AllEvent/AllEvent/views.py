from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'MeuSite/home.html')
def cadastro(request):
    # Se o usuário já estiver logado, não tem por que ele ver a página de cadastro.
    if request.user.is_authenticated:
        return redirect('home')

    # Esta parte só executa quando o botão "CRIAR CONTA" é pressionado
    if request.method == 'POST':
        # 1. PEGAR OS DADOS DO FORMULÁRIO
        nome = request.POST.get('nome_completo')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        senha_confirm = request.POST.get('password_confirm')

        # 2. VALIDAR OS DADOS
        if senha != senha_confirm:
            messages.error(request, 'As senhas não coincidem!')
            return redirect('cadastro') # Volta para a pág. de cadastro com a mensagem de erro

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está em uso.')
            return redirect('cadastro') # Volta para a pág. de cadastro com a mensagem de erro
        
        # 3. CRIAR O USUÁRIO (se tudo estiver OK)
        # Usamos o email como username também, é um padrão comum e seguro
        user = User.objects.create_user(username=email, email=email, password=senha)
        user.first_name = nome # Opcional: guardar o nome completo
        user.save()

        # Faz o login do novo usuário automaticamente
        login(request, user)

        # 4. ADICIONAR MENSAGEM DE SUCESSO
        messages.success(request, 'Conta criada com sucesso!')

        # 5. REDIRECIONAR PARA A HOME
        return redirect('home')

    # Se o método não for POST (ou seja, o usuário só abriu a página), apenas renderize o HTML
    return render(request, 'MeuSite/cadastro.html')

    return render(request, 'MeuSite/cadastro.html')
@login_required
def editar_dados_view(request):
    return render(request, 'MeuSite/editar-dados.html')
@login_required
def favoritos_view(request):
    return render(request, 'MeuSite/favoritos.html')
@login_required
def perfil_view(request):
    return render(request, 'MeuSite/perfil.html')
@login_required
def preferencias_view(request):
    return render(request, 'MeuSite/preferencias.html')
def lista_view(request):
    return render(request, 'MeuSite/lista.html')
def event_view(request):
    return render(request, 'MeuSite/event.html')