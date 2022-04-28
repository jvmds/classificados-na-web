import datetime
import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class TipoAnuncio(models.Model):
    nome = models.CharField(max_length=100)
    quantidadePalavras = models.PositiveIntegerField()
    imagem = models.BooleanField()

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('categorias', args=[str(self.id)])

    def __str__(self):
        return self.nome


class Anuncio(models.Model):

    tipo_anuncio = models.ForeignKey('TipoAnuncio', models.CASCADE, null=True, help_text='Exemplo')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=50, help_text='Exemplo')
    valor = models.DecimalField(max_digits=10, decimal_places=2, help_text='Exemplo')
    descricao = models.TextField(max_length=500, null=True, blank=True, help_text='Exemplo')
    telefone1 = models.CharField(max_length=11, help_text='Exemplo')
    telefone2 = models.CharField(max_length=11, null=True, blank=True, help_text='Exemplo')
    observacao = models.CharField(max_length=25, null=True, blank=True, help_text='Exemplo')
    imagem = models.ImageField(null=True, blank=True)
    data_criacao = models.DateField(auto_now_add=True)
    categoria = models.ManyToManyField('Categoria', help_text='Exemplo')
    user = models.ForeignKey(User, models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('detalhes-anuncio:pk', kwargs={'pk': str(self.id)})

    def disponibilidade_anuncio(self):
        return datetime.date.today() - self.data_criacao <= datetime.timedelta(days=3)

    def __str__(self):
        return self.titulo