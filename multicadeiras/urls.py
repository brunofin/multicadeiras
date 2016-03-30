# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()



urlpatterns = patterns('',
    url(r'^$', 'produto.views.home'), # Index padrao
    url(r'^conteudo/quemsomos$', 'produto.views.quemsomos'),
    url(r'^conteudo/clientes$', 'produto.views.clientes'),
    url(r'^conteudo/galeria$', 'produto.views.galeria'),
    url(r'^conteudo/contato$', 'produto.views.contato'),
    url(r'^buscar$', 'produto.views.buscar'),
    url(r'^produto/(?P<produto_id>\d*)$', 'produto.views.produtoDetalhes'),
    url(r'^subcategoria/(?P<subcategoria_id>\d*)$', 'produto.views.subcategoriaListar'),
    url(r'^admin/$', 'admin.views.adminHome'), # Login administrativo
    url(r'^admin/main/$', 'admin.views.adminMain'), # Index Administrativo
    url(r'^admin/logout/$', 'admin.views.adminLogout'),
    url(r'^admin/categoria/cadastrar/$', 'admin.views.categoriaCadastrar'),
    url(r'^admin/categoria/listar/$', 'admin.views.categoriaListar'),
    url(r'^admin/categoria/editar/(?P<categoria_id>\d*)$', 'admin.views.categoriaEditar'),
    url(r'^admin/categoria/remover/(?P<categoria_id>\d*)$', 'admin.views.categoriaRemover'),
    url(r'^admin/subcategoria/cadastrar/$', 'admin.views.subcategoriaCadastrar'),
    url(r'^admin/subcategoria/listar/$', 'admin.views.subcategoriaListar'),
    url(r'^admin/subcategoria/editar/(?P<subcategoria_id>\d*)$', 'admin.views.subcategoriaEditar'),
    url(r'^admin/subcategoria/remover/(?P<subcategoria_id>\d*)$', 'admin.views.subcategoriaRemover'),
    url(r'^admin/produto/cadastrar/$', 'admin.views.produtoCadastrar'),
    url(r'^admin/produto/listar/$', 'admin.views.produtoListar'),
    url(r'^admin/produto/editar/(?P<produto_id>\d*)$', 'admin.views.produtoEditar'),
    url(r'^admin/produto/remover/(?P<produto_id>\d*)$', 'admin.views.produtoRemover'),
    url(r'^admin/produto/destaques/$', 'admin.views.produtoDestaqueCriarEditar'),
    url(r'^admin/slideshow/$', 'admin.views.slideshowCriarEditar'),
    url(r'^admin/menu/ordem/$', 'admin.views.menuOrdem'),
    url(r'^admin/galeria/cadastrar/$', 'admin.views.cadastrarGaleria'),
    url(r'^admin/galeria/remover/(?P<foto_id>\d*)$', 'admin.views.removerGaleria'),
    url(r'^admin/galeria/listar/$', 'admin.views.listarGaleria'),
    url(r'^admin/galeria/editar/(?P<foto_id>\d*)$', 'admin.views.editarGaleria'),
    url(r'^admin/clientes$', 'admin.views.clientesMain'),
    url(r'^admin/clientes/cadastro', 'admin.views.clientesCadastro'),
    url(r'^admin/clientes/remover/(?P<cliente_id>\d*)$', 'admin.views.clientesRemover'),
    url(r'^admin/clientes/categorias$', 'admin.views.clientesCategMain'),
    url(r'^admin/clientes/categorias/cadastro', 'admin.views.clientesCategCadastro'),
    url(r'^admin/clientes/categorias/remover/(?P<categoria_id>\d*)$', 'admin.views.clientesCategRemover'),
    url(r'^admin/busca$', r'admin.views.resultadosBuscas'),
    url(r'^admin/relatorio$', r'admin.views.relatorio'),
)

urlpatterns += staticfiles_urlpatterns()

