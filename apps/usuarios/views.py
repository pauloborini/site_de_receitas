from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from apps.receitas.models import Receita


# Create your views here.
def cadastro(request):
    """Cadastra um novo usuário"""
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request, 'Preencha os campos corretamente')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request, 'Preencha os campos corretamente')
            return redirect('cadastro')
        if not senha == senha2:
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Nome de usuário já existe')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    """Realiza login no site"""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Preencha os campos para efetuar login')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            username = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=username, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
        print('E-mail ou senha inválidos')
    return render(request, 'usuarios/login.html')


def dashboard(request):
    """Pagina Inicial do usuario"""
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)
        paginator = Paginator(receitas, 3)
        page = request.GET.get('page')
        receitas_por_pagina = paginator.get_page(page)
        dados = {
            'receitas': receitas_por_pagina
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index.html')


def logout(request):
    """Realiza logout do site"""
    auth.logout(request)
    return render(request, 'usuarios/login.html')


def cria_receita(request):
    """Usuario cria uma receita"""
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_de_preparo = request.POST['modo_de_preparo']
        tempo_de_preparo = request.POST['tempo_de_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        if campo_vazio(nome_receita) or campo_vazio(ingredientes) or campo_vazio(modo_de_preparo) or campo_vazio(
                tempo_de_preparo) or campo_vazio(rendimento) or campo_vazio(categoria):
            messages.error(request, 'Preencha todos os campos, clique em Voltar para tentar novamente.')
            return redirect('cria_receita')
        else:
            user = get_object_or_404(User, pk=request.user.id)
            receita = Receita.objects.create(pessoa=user,
                                             nome_receita=nome_receita, ingredientes=ingredientes,
                                             modo_de_preparo=modo_de_preparo, tempo_de_preparo=tempo_de_preparo,
                                             rendimento=rendimento, categoria=categoria,
                                             foto_receita=foto_receita)
            receita.save()
            return redirect('dashboard')

    else:
        return render(request, 'usuarios/cria_receita.html')


def campo_vazio(campo):
    return not campo.strip()


def deleta_receita(request, receita_id):
    """Deleta receita criada pelo usuario"""
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')


def edita_receita(request, receita_id):
    """Entra na edição da receita criada pelo usuario"""

    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = {
        'receita': receita
    }
    return render(request, 'usuarios/edita_receita.html', receita_a_editar)


def atualiza_receita(request):
    """Atualiza de fato a receita criada pelo usuario"""

    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        r = Receita.objects.get(pk=receita_id)
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_de_preparo = request.POST['modo_de_preparo']
        r.tempo_de_preparo = request.POST['tempo_de_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            r.foto_receita = request.FILES['foto_receita']
        if campo_vazio(r.nome_receita) or campo_vazio(r.ingredientes) or campo_vazio(r.modo_de_preparo) or campo_vazio(
                r.tempo_de_preparo) or campo_vazio(r.rendimento) or campo_vazio(r.categoria):
            messages.error(request, 'Preencha todos os campos')
            return redirect('edita_receita', receita_id)
        r.save()
        return redirect('dashboard')
