# -*- coding: UTF-8 -*-
from django.db import models
from multicadeiras.storage import OverwriteStorage

class ClienteCategoria(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=255)
    
class Cliente(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=255)
    website = models.URLField(null = True)
    categoria = models.ForeignKey(ClienteCategoria)

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=50)

class Subcategoria(models.Model):
    id = models.AutoField(primary_key = True)
    categoria = models.ForeignKey(Categoria)
    nome = models.CharField(max_length = 50)

class Produto(models.Model):
    id = models.AutoField(primary_key = True)
    subcategoria = models.ForeignKey(Subcategoria)
    nome = models.CharField(max_length = 100)
    ativo = models.BooleanField()
    descricao = models.CharField(max_length = 255)
    imagem = models.ImageField(upload_to = 'upload/produto')

class Slideshow(models.Model):
    id = models.AutoField(primary_key = True)
    imagem1 = models.ImageField(upload_to = 'slideshow', storage=OverwriteStorage())
    imagem2 = models.ImageField(upload_to = 'slideshow', storage=OverwriteStorage())
    imagem3 = models.ImageField(upload_to = 'slideshow', storage=OverwriteStorage())
    imagem4 = models.ImageField(upload_to = 'slideshow', storage=OverwriteStorage())

class OrdemMenu(models.Model):
    id = models.AutoField(primary_key = True)
    ordem = models.CharField(max_length = 20)

class Destaque(models.Model):
    id = models.AutoField(primary_key = True)
    produto01 = models.ForeignKey(Produto, related_name = 'destaque_produto01')
    produto02 = models.ForeignKey(Produto, related_name = 'destaque_produto02')
    produto03 = models.ForeignKey(Produto, related_name = 'destaque_produto03')
    produto04 = models.ForeignKey(Produto, related_name = 'destaque_produto04')
    produto05 = models.ForeignKey(Produto, related_name = 'destaque_produto05')
    produto06 = models.ForeignKey(Produto, related_name = 'destaque_produto06')
    produto07 = models.ForeignKey(Produto, related_name = 'destaque_produto07')
    produto08 = models.ForeignKey(Produto, related_name = 'destaque_produto08')
    produto09 = models.ForeignKey(Produto, related_name = 'destaque_produto09')
    produto10 = models.ForeignKey(Produto, related_name = 'destaque_produto10')
    produto11 = models.ForeignKey(Produto, related_name = 'destaque_produto11')
    produto12 = models.ForeignKey(Produto, related_name = 'destaque_produto12')

class TermoBusca(models.Model):
    id = models.AutoField(primary_key = True)
    termo = models.CharField(max_length = 255)
    quantidade = models.PositiveIntegerField()

class FotoGaleria(models.Model):
    id = models.AutoField(primary_key = True)
    foto = models.ImageField(upload_to = 'galeria')
    nome = models.CharField(max_length = 100)