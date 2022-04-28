from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Anuncio, TipoAnuncio


class CriarAnuncioForm(forms.ModelForm):

    class Meta:
        model = Anuncio
        exclude = ['user']

    def clean_descricao(self):
        descricao = self.cleaned_data['descricao']
        tipo_anuncio = self.cleaned_data['tipo_anuncio']
        
        if len(descricao.strip().split()) > tipo_anuncio.quantidadePalavras:
            raise ValidationError('Tamanho não coresponde')
        return descricao

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_anuncio'].widget.attrs['class'] = 'form-select'
        self.fields['titulo'].widget.attrs['class'] = 'form-control'
        self.fields['valor'].widget.attrs['class'] = 'form-control'
        self.fields['descricao'].widget.attrs['class'] = 'form-control'
        self.fields['telefone1'].widget.attrs['class'] = 'form-control'
        self.fields['telefone2'].widget.attrs['class'] = 'form-control'
        self.fields['observacao'].widget.attrs['class'] = 'form-control'
        self.fields['categoria'].widget.attrs['class'] = 'form-control'


class CadastroUsuarioForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
