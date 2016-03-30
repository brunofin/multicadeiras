# -*- coding: UTF-8 -*-
from django import forms
from django.core.files.images import get_image_dimensions

from models import *

class CategoriaChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nome

class SubcategoriaChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.categoria.nome + ' -> ' + obj.nome
    
class ProdutoChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.subcategoria.categoria.nome + ' -> ' + obj.subcategoria.nome + ' -> ' + obj.nome
    
class ClienteCategoriaForm(forms.ModelForm):
    class Meta:
        model = ClienteCategoria

class ClienteForm(forms.ModelForm):
    categoria = CategoriaChoiceField(queryset=ClienteCategoria.objects.all())
    website = forms.URLField(required = False)
    
    class Meta:
        model = Cliente

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        exclude = ('ordem',)

class SubcategoriaForm(forms.ModelForm):
    categoria = CategoriaChoiceField(queryset=Categoria.objects.all(), label="Categoria pertencente")
        
    class Meta:
        model = Subcategoria

class ProdutoForm(forms.ModelForm):
    descricao = forms.CharField(widget=forms.Textarea, label="Descrição")
    ativo = forms.BooleanField(initial=True)
    imagem = forms.ImageField(required=False)
    
    class Meta:
        model = Produto
        exclude = ('subcategoria',)

class GaleriaForm(forms.ModelForm):
    class Meta:
        model = FotoGaleria

class GaleriaEditForm(forms.ModelForm):
    class Meta:
        model = FotoGaleria
        exclude = ('foto',)

class SlideshowForm(forms.ModelForm):
    imagem1 = forms.ImageField(label = "Primeira imagem")
    imagem2 = forms.ImageField(label = "Segunda imagem")
    imagem3 = forms.ImageField(label = "Terceira imagem")
    imagem4 = forms.ImageField(label = "Quarta imagem")
    class Meta:
        model = Slideshow
    def clean_imagem1(self):
        imagem1 = self.cleaned_data['imagem1']
        if not imagem1:
            return imagem1
        else:
            w, h = get_image_dimensions(imagem1)
            if w != 1050 or h != 315:
                raise forms.ValidationError("A imagem deve ser de 1050x315 pixels.")
        return imagem1
    
    def clean_imagem2(self):
        imagem2 = self.cleaned_data['imagem2']
        if not imagem2:
            return imagem2
        else:
            w, h = get_image_dimensions(imagem2)
            if w != 1050 or h != 315:
                raise forms.ValidationError("A imagem deve ser de 1050x315 pixels.")
        return imagem2
    
    def clean_imagem3(self):
        imagem3 = self.cleaned_data['imagem3']
        if not imagem3:
            return imagem3
        else:
            w, h = get_image_dimensions(imagem3)
            if w != 1050 or h != 315:
                raise forms.ValidationError("A imagem deve ser de 1050x315 pixels.")
        return imagem3
    
    def clean_imagem4(self):
        imagem4 = self.cleaned_data['imagem4']
        if not imagem4:
            return imagem4
        else:
            w, h = get_image_dimensions(imagem4)
            if w != 1050 or h != 315:
                raise forms.ValidationError("A imagem deve ser de 1050x315 pixels.")
        return imagem4

class SlideshowFormEdit(SlideshowForm):
    imagem1 = forms.ImageField(label = "Primeira imagem", required=False)
    imagem2 = forms.ImageField(label = "Segunda imagem", required=False)
    imagem3 = forms.ImageField(label = "Terceira imagem", required=False)
    imagem4 = forms.ImageField(label = "Quarta imagem", required=False)

class DestaqueForm(forms.ModelForm):
    produto01 = ProdutoChoiceField(queryset=Produto.objects.all().order_by("subcategoria"), empty_label="Selecione", label="Produto em destaque 1")
    produto02 = ProdutoChoiceField(queryset=Produto.objects.all().order_by("subcategoria"), empty_label="Selecione", label="Produto em destaque 2")
    produto03 = ProdutoChoiceField(queryset=Produto.objects.all().order_by("subcategoria"), empty_label="Selecione", label="Produto em destaque 3")
    produto04 = ProdutoChoiceField(queryset=Produto.objects.all().order_by("subcategoria"), empty_label="Selecione", label="Produto em destaque 4")
    produto05 = ProdutoChoiceField(queryset=Produto.objects.all().order_by("subcategoria"), empty_label="Selecione", label="Produto em destaque 5")
    produto06 = ProdutoChoiceField(queryset=Produto.objects.all().order_by("subcategoria"), empty_label="Selecione", label="Produto em destaque 6")
    produto07 = ProdutoChoiceField(queryset=Produto.objects.all().order_by("subcategoria"), empty_label="Selecione", label="Produto em destaque 7")
    produto08 = ProdutoChoiceField(queryset=Produto.objects.all().order_by("subcategoria"), empty_label="Selecione", label="Produto em destaque 8")
    produto09 = ProdutoChoiceField(queryset=Produto.objects.all().order_by("subcategoria"), empty_label="Selecione", label="Produto em destaque 9")
    produto10 = ProdutoChoiceField(queryset=Produto.objects.all().order_by("subcategoria"), empty_label="Selecione", label="Produto em destaque 10")
    produto11 = ProdutoChoiceField(queryset=Produto.objects.all().order_by("subcategoria"), empty_label="Selecione", label="Produto em destaque 11")
    produto12 = ProdutoChoiceField(queryset=Produto.objects.all().order_by("subcategoria"), empty_label="Selecione", label="Produto em destaque 12")

    class Meta:
        model = Destaque
