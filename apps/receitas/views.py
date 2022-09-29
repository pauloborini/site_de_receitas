from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Receita


def index(request):
    """Pagina inicial do site"""
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    paginator = Paginator(receitas, 6)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)
    dados = {
        'receitas': receitas_por_pagina
    }
    return render(request, 'index.html', dados)


def receita(request, receita_id):
    """Pagina onde a receita aparece"""
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_exibir = {
        'receita': receita
    }
    return render(request, 'receita.html', receita_a_exibir)


def buscar(request):
    """Sistema de busca do site"""
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)
    dados = {
        'receitas': lista_receitas
    }
    return render(request, 'buscar.html', dados)
