# -*- coding: UTF-8 -*-

from django.shortcuts import render
from multicadeiras.produto.models import OrdemMenu, Categoria, Subcategoria, \
    Destaque, Produto, TermoBusca, FotoGaleria, Cliente, ClienteCategoria
from django.utils.datastructures import MultiValueDictKeyError

def getOrdemMenu():
    try:
        ordemAux = OrdemMenu.objects.get(pk=1).ordem.split(',')
        ordem = [int(numero) for numero in ordemAux]
    except:
        ordem = []
    return ordem

def getDestaques():
    try:
        destaques = Destaque.objects.all()[0]
    except:
        destaques = []
    return destaques

def home(request):
    categorias = Categoria.objects.all()
    subcategorias = Subcategoria.objects.all().order_by('nome')
        
    return render(request, 'multicadeiras/index.html', {'slideativo': True, 'ordem': getOrdemMenu(), 'cat': categorias, 'subcat': subcategorias, 'destaques': getDestaques()})

def quemsomos(request):
    categorias = Categoria.objects.all()
    subcategorias = Subcategoria.objects.all().order_by('nome')
    
    return render(request, 'multicadeiras/quemSomos.html', {'ordem': getOrdemMenu(), 'cat': categorias, 'subcat': subcategorias})

def clientes(request):
    categorias = Categoria.objects.all()
    subcategorias = Subcategoria.objects.all().order_by('nome')
    clientesCat = ClienteCategoria.objects.all()
    clientes = Cliente.objects.all().order_by('nome')
    
    return render(request, 'multicadeiras/clientes.html', {'ordem': getOrdemMenu(), 'cat': categorias, 'subcat': subcategorias, 'clienteCat': clientesCat, 'clientes': clientes})

def galeria(request):
    categorias = Categoria.objects.all()
    subcategorias = Subcategoria.objects.all().order_by('nome')
    galeria = FotoGaleria.objects.all().order_by('nome')
    
    return render(request, 'multicadeiras/galeria.html', {'ordem': getOrdemMenu(), 'cat': categorias, 'subcat': subcategorias, 'galeria': galeria})

def contato(request):
    categorias = Categoria.objects.all()
    subcategorias = Subcategoria.objects.all().order_by('nome')
    
    return render(request, 'multicadeiras/contato.html', {'ordem': getOrdemMenu(), 'cat': categorias, 'subcat': subcategorias})

def produtoDetalhes(request, produto_id):
    categorias = Categoria.objects.all()
    subcategorias = Subcategoria.objects.all().order_by('nome')
    
    produto = Produto.objects.get(pk=produto_id)
    return render(request, 'multicadeiras/produto/produto.html', {'ordem': getOrdemMenu(), 'cat': categorias, 'subcat': subcategorias, 'produto': produto})

def subcategoriaListar(request, subcategoria_id):
    categorias = Categoria.objects.all()
    subcategorias = Subcategoria.objects.all().order_by('nome')
    
    produtosAux = Produto.objects.all().order_by('nome')
    produtos = []
    for produto in produtosAux:
        if produto.subcategoria.id == int(subcategoria_id):
            produtos.append(produto)      
    return render(request, 'multicadeiras/listarProdutos.html', {'ordem': getOrdemMenu(), 'cat': categorias, 'subcat': subcategorias, 'produtos': produtos})

def buscar(request):
    categorias = Categoria.objects.all()
    subcategorias = Subcategoria.objects.all().order_by('nome')
    
    try:
        query = request.GET['q']
        
        termos = TermoBusca.objects.all()
        
        achou = False
        for termo in termos:
            if termo.termo.lower() == query.lower():
                termo.quantidade = termo.quantidade + 1
                termo.save()
                achou = True
                break
        
        if not achou:
            termo = TermoBusca()
            termo.quantidade = 1
            termo.termo = query.lower()
            termo.save()
        
        produtos = Produto.objects.all()
        resultadosBusca = []
        
        for produto in produtos:
            if query.lower() in produto.nome.lower() or query.lower() in produto.descricao.lower():
                resultadosBusca.append(produto)
        
        if len(resultadosBusca) == 0:
            return render(request, 'multicadeiras/busca/nenhumResultado.html', {'ordem': getOrdemMenu(), 'cat': categorias, 'subcat': subcategorias})
        else:
            return render(request, 'multicadeiras/busca/resultados.html', {'ordem': getOrdemMenu(), 'cat': categorias, 'subcat': subcategorias, 'resultados': resultadosBusca})
        
    except MultiValueDictKeyError:
        return render(request, 'multicadeiras/busca/nenhumResultado.html', {'ordem': getOrdemMenu(), 'cat': categorias, 'subcat': subcategorias})	
