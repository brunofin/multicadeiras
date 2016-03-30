# -*- coding: UTF-8 -*-
from django import forms
from django.contrib.auth.models import User
from multicadeiras.produto.models import Categoria, OrdemMenu

class admLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User

class OrdemMenuForm(forms.ModelForm):
    ordem = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = OrdemMenu