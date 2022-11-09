from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormAluno

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['senha']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Você está logado')
            return redirect('dashboard')
        else:
            messages.error(request, 'Erro ao logar')
            return redirect('login')

    return render(request, 'accounts/login.html')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    user = request.POST.get('user')
    senha = request.POST.get('password')
    senha2 = request.POST.get('password2')

    if not nome or not email or not user or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio')
        return render(request, 'accounts/cadastro.html')
    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter no mínimo 6 caracteres')
        return render(request, 'accounts/cadastro.html')

    if senha != senha2:
        messages.error(request, 'Senhas não conferem')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=user).exists():
        messages.error(request, 'Usuário já existe')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, 'Registrado com sucesso')

    first_name = nome.split(' ')[0]

    last_name = nome.split(' ', 1)[1] if nome.count(' ') > 0 else ''
    user = User.objects.create_user(
        username=user, email=email, password=senha, first_name=first_name, last_name=last_name)
    user.save()
    return redirect('login')


def logout(request):
    auth.logout(request)
    return redirect('dashboard')


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormAluno()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormAluno(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao cadastrar aluno')
        form = FormAluno(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    return redirect('dashboard')
