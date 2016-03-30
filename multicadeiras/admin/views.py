# -*- coding: UTF-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.utils.datastructures import MultiValueDictKeyError

from forms import admLoginForm
from multicadeiras.admin.forms import OrdemMenuForm
from multicadeiras.produto.forms import CategoriaForm, SubcategoriaForm, \
    ProdutoForm, SlideshowForm, DestaqueForm, SlideshowFormEdit, GaleriaForm, \
    ClienteForm, ClienteCategoriaForm, GaleriaEditForm
from multicadeiras.produto.models import Categoria, Subcategoria, Produto, \
    Slideshow, OrdemMenu, Destaque, FotoGaleria, Cliente, ClienteCategoria, \
    TermoBusca


def adminHome(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/admin/main/')
    else:
        if request.method == 'POST':
            form = admLoginForm(request.POST)
            if form.is_valid():
                user = authenticate(username=request.POST['username'], password=request.POST['password'])
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/admin/main/')
                else:
                    # login invalido
                    return HttpResponseRedirect('/admin/')
        else:
            form = admLoginForm()
            return render(request, 'admin/login.html', {'form': form})

@user_passes_test(lambda u : u.is_superuser)
def clientesMain(request):
    form = ClienteForm()
    clientes = Cliente.objects.all();
    categorias = ClienteCategoria.objects.all()
    return render(request, 'admin/clientes/listar.html', {'form': form, 'clientes': clientes, 'categorias': categorias})

@user_passes_test(lambda u : u.is_superuser)
def clientesCadastro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return clientesMain(request)
        else:
            return render(request, 'admin/erro_form.html', {'errors': form.errors})

@user_passes_test(lambda u : u.is_superuser)
def clientesRemover(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    cliente.delete()
    return clientesMain(request)

@user_passes_test(lambda u : u.is_superuser)
def clientesCategMain(request):
    form = ClienteCategoriaForm()
    categorias = ClienteCategoria.objects.all()
    return render(request, 'admin/clientes/categ_cadastro.html', {'form': form, 'categorias': categorias})

@user_passes_test(lambda u : u.is_superuser)
def clientesCategCadastro(request):
    if request.method == 'POST':
        form = ClienteCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return clientesCategMain(request)
        else:
            return render(request, 'admin/erro_form.html', {'errors': form.errors})
    
@user_passes_test(lambda u : u.is_superuser)
def clientesCategRemover(request, categoria_id):
    categoria = ClienteCategoria.objects.get(pk=categoria_id)
    categoria.delete()
    return clientesCategMain(request)

@user_passes_test(lambda u : u.is_superuser)
def adminMain(request):
    return render_to_response('admin/index.html')

@login_required
def adminLogout(request):
    logout(request)
    return HttpResponseRedirect('/admin/')

@user_passes_test(lambda u : u.is_superuser)
def categoriaCadastrar(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/categoria/listar/')
        else:
            return render(request, 'admin/erro_form.html', {'errors': form.errors })
    else:
        form = CategoriaForm()
        return render(request, 'admin/categoria/cadastrar.html', {'form': form})

@user_passes_test(lambda u : u.is_superuser)
def categoriaListar(request):
    categorias = Categoria.objects.all()
    return render(request, 'admin/categoria/listar.html', {'categorias': categorias})

@user_passes_test(lambda u : u.is_superuser)
def categoriaEditar(request, categoria_id):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.id = categoria_id
            categoria.save()
            return HttpResponseRedirect('/admin/categoria/listar')
        else:
            return render(request, 'admin/erro_form.html', {'errors': form.errors })
    else:
        categoria = Categoria.objects.get(pk=categoria_id)
        form = CategoriaForm(instance=categoria)
        return render(request, 'admin/categoria/editar.html', {'form': form, 'categoria': categoria})

@user_passes_test(lambda u : u.is_superuser)
def categoriaRemover(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    categoria.delete()
    return HttpResponseRedirect('/admin/categoria/listar')

@user_passes_test(lambda u : u.is_superuser)
def subcategoriaCadastrar(request):
    if request.method == 'POST':
        form = SubcategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/subcategoria/listar/')
        else:
            return render(request, 'admin/erro_form.html', {'errors': form.errors })
    else:
        form = SubcategoriaForm()
        return render(request, 'admin/subcategoria/cadastrar.html', {'form': form})

@user_passes_test(lambda u : u.is_superuser)
def subcategoriaListar(request):
    categorias = Categoria.objects.all()
    subcategorias = Subcategoria.objects.all()
    return render(request, 'admin/subcategoria/listar.html', {'categorias': categorias, 'subcategorias': subcategorias})

@user_passes_test(lambda u : u.is_superuser)
def subcategoriaEditar(request, subcategoria_id):
    if request.method == 'POST':
        form = SubcategoriaForm(request.POST)
        if form.is_valid():
            subcategoria = form.save(commit=False)
            subcategoria.id = subcategoria_id
            subcategoria.save()
            return HttpResponseRedirect('/admin/subcategoria/listar')
        else:
            return render(request, 'admin/erro_form.html', {'errors': form.errors })
    else:
        subcategoria = Subcategoria.objects.get(pk=subcategoria_id)
        form = SubcategoriaForm(instance=subcategoria)
        return render(request, 'admin/subcategoria/editar.html', {'form': form, 'subcategoria': subcategoria})

@user_passes_test(lambda u : u.is_superuser)
def subcategoriaRemover(request, subcategoria_id):
    subcategoria = Subcategoria.objects.get(pk=subcategoria_id)
    subcategoria.delete()
    return HttpResponseRedirect('/admin/subcategoria/listar')

@user_passes_test(lambda u : u.is_superuser)
def produtoCadastrar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.subcategoria = Subcategoria.objects.get(pk=int(form.data['subcategoria']))
            produto.save()
            return HttpResponseRedirect('/admin/produto/listar/')
        else:
            return render(request, 'admin/erro_form.html', {'errors': form.errors })
    else:
        categorias = Categoria.objects.all()
        subcategorias = Subcategoria.objects.all()
        form = ProdutoForm()
        return render(request, 'admin/produto/cadastrar.html', {'form': form, 'categ': categorias, 'subcateg': subcategorias})

@user_passes_test(lambda u : u.is_superuser)
def produtoListar(request):
    categorias = Categoria.objects.all()
    subcategorias = Subcategoria.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'admin/produto/listar.html', {'categorias': categorias, 'subcategorias': subcategorias, 'produtos': produtos})

@user_passes_test(lambda u : u.is_superuser)
def produtoEditar(request, produto_id):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.id = produto_id
            produto.subcategoria = Subcategoria.objects.get(pk=request.POST['subcategoria'])
            
            try:
                produto.imagem = request.FILES['imagem']
            except:
                produto.imagem = Produto.objects.get(pk=produto.id).imagem
            
            produto.save()
            return HttpResponseRedirect('/admin/produto/listar')
        else:
            return render(request, 'admin/erro_form.html', {'errors': form.errors })
    else:
        categorias = Categoria.objects.all()
        subcategorias = Subcategoria.objects.all()
        produto = Produto.objects.get(pk=produto_id)
        form = ProdutoForm(instance=produto)
        return render(request, 'admin/produto/editar.html', {'form': form, 'categ': categorias, 'subcateg': subcategorias, 'produto': produto})

@user_passes_test(lambda u : u.is_superuser)
def produtoRemover(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    produto.delete()
    return HttpResponseRedirect('/admin/produto/listar')

@user_passes_test(lambda u : u.is_superuser)
def slideshowCriarEditar(request):    
    if request.method == 'POST':
        try:
            request.FILES['imagem1'].name = '1.png'
        except MultiValueDictKeyError:
            pass
        try:
            request.FILES['imagem2'].name = '2.png'
        except MultiValueDictKeyError:
            pass
        try:
            request.FILES['imagem3'].name = '3.png'
        except MultiValueDictKeyError:
            pass
        try:
            request.FILES['imagem4'].name = '4.png'
        except MultiValueDictKeyError:
            pass
        
        form = SlideshowFormEdit(request.POST, request.FILES)
        if form.is_valid():
            slideshow = form.save(commit=False)
            slideshow.id = 1            
            slideshow.save()
            return HttpResponseRedirect('/admin/')
        else:
            return render(request, 'admin/erro_form.html', {'errors': form.errors })
    else:
        form = None
        try:
            slideshow = Slideshow.objects.get(pk=1)
            form = SlideshowFormEdit(instance=slideshow)
        except ObjectDoesNotExist:
            form = SlideshowForm()
        return render(request, 'admin/slideshow/criar_editar.html', {'form': form})

@user_passes_test(lambda u : u.is_superuser)
def menuOrdem(request):
    if request.method == 'POST':
        form = OrdemMenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.id = 1
            menu.save()
            return HttpResponseRedirect('/admin/')
        else:
            return render(request, 'admin/erro_form.html', {'errors': form.errors })
    else:
        form = None
        try:
            ordem = OrdemMenu.objects.get(pk=1)
            form = OrdemMenuForm(instance=ordem)
        except ObjectDoesNotExist:
            form = OrdemMenuForm()
        categorias = Categoria.objects.all();
        return render(request, 'admin/menu/ordem.html', {'categorias': categorias, 'form': form})

@user_passes_test(lambda u : u.is_superuser)
def produtoDestaqueCriarEditar(request):
    if request.method == 'POST':
        form = DestaqueForm(request.POST)
        if form.is_valid():
            destaques = form.save(commit=False)
            destaques.id = 1
            destaques.save()
            return HttpResponseRedirect('/admin/')
        else:
            return render(request, 'admin/erro_form.html', {'errors': form.errors })
    else:
        form = None
        try:
            destaques = Destaque.objects.get(pk=1)
            form = DestaqueForm(instance=destaques)
        except ObjectDoesNotExist:
            form = DestaqueForm()
        return render(request, 'admin/produto/destaques.html', {'form': form})

@user_passes_test(lambda u : u.is_superuser)
def cadastrarGaleria(request):
    if request.method == 'POST':
        form = GaleriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/')
        else:
            return render(request, 'admin/erro_form.html', {'errors': form.errors })
    else:
        form = GaleriaForm()
        return render(request, 'admin/galeria/cadastrar.html', {'form': form})

@user_passes_test(lambda u : u.is_superuser)
def removerGaleria(request, foto_id):
    foto = FotoGaleria.objects.get(pk = foto_id)
    foto.delete()
    return HttpResponseRedirect('/admin/galeria/listar')

@user_passes_test(lambda u : u.is_superuser)
def listarGaleria(request):
    galeria = FotoGaleria.objects.all().order_by('nome')
    return render(request, 'admin/galeria/listar.html', {'galeria': galeria})

@user_passes_test(lambda u : u.is_superuser)
def editarGaleria(request, foto_id):
    if request.method == 'POST':
        form = GaleriaEditForm(request.POST)
        if form.is_valid():
            galeria = form.save(commit=False)
            galeria.id = foto_id
            galeria.foto = FotoGaleria.objects.get(pk = foto_id).foto
            galeria.save()
            return HttpResponseRedirect('/admin/galeria/listar')
        else:
            return render(request, 'admin/erro_form.html', {'errors': form.errors })
    else:
        galeria = FotoGaleria.objects.get(pk = foto_id)
        form = GaleriaEditForm(instance=galeria)
        return render(request, 'admin/galeria/cadastrar.html', {'form': form})

@user_passes_test(lambda u : u.is_superuser)
def resultadosBuscas(request):
    resultados = TermoBusca.objects.all().order_by('-quantidade')
    
    return render(request, 'admin/analise/resultadosBuscas.html', {'resultados': resultados})

@user_passes_test(lambda u : u.is_superuser)
def relatorio(request):
    return render(request, 'admin/analise/relatorio.html')