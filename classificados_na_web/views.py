from PIL import Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User, Group
from django.contrib.auth import views as auth_view

from classificados_na_web.models import Anuncio
from .forms import CriarAnuncioForm, CadastroUsuarioForm


class IndexView(LoginRequiredMixin, generic.ListView):

    context_object_name = 'anuncios'
    template_name = 'classificados-na-web/index.html'
    paginate_by = 10

    def get_queryset(self):
        return Anuncio.objects.all()


class PerfilView(LoginRequiredMixin, generic.ListView):
    model = User
    context_object_name = 'anuncios'
    template_name = 'classificados-na-web/perfil.html'


class DetalhesAnuncioView(LoginRequiredMixin, generic.DetailView):
    model = Anuncio
    context_object_name = 'anuncio'
    template_name = 'classificados-na-web/detalhes-anuncio.html'


class CriarAnuncioView(LoginRequiredMixin, generic.CreateView):
    template_name = 'classificados-na-web/anuncio_form.html'
    form_class = CriarAnuncioForm
    model = Anuncio
    success_url = reverse_lazy('classificados-na-web:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.success_url = reverse_lazy('classificados-na-web:d-anuncio', kwargs={'pk': form.instance.id})
        return super().form_valid(form)


class HistoricoView(LoginRequiredMixin, generic.ListView):

    model = Anuncio
    template_name = 'classificados-na-web/historico_list.html'

    def get_queryset(self):
        return Anuncio.objects.filter(user=self.request.user.id)


class CadastroView(generic.CreateView):

    model = User
    template_name = 'classificados-na-web/cadastro.html'
    form_class = CadastroUsuarioForm
    success_url = reverse_lazy('login')


def obter_imagem(request, id_anuncio):
    anuncio = get_object_or_404(Anuncio, pk=id_anuncio)
    resposta = HttpResponse(content_type='image/png')
    imagem = Image.open(anuncio.imagem)
    imagem.save(resposta, 'png')
    return resposta
