from django.urls import path

from . import views

app_name = 'classificados-na-web'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detalhes-anuncio/<str:pk>/', views.DetalhesAnuncioView.as_view(), name='d-anuncio'),
    path('perfil/<str:pk>/', views.PerfilView.as_view(), name='perfil-usuario'),
    path('criar-anuncio/', views.CriarAnuncioView.as_view(), name='criar-anuncio'),
    path('imagem/<str:id_anuncio>', views.obter_imagem, name='imagem-anuncio'),
    path('historico/', views.HistoricoView.as_view(), name='historico-anuncio'),
    path('cadastro/', views.CadastroView.as_view(), name='cadastro-usuario')
]
