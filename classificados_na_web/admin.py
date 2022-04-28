from django.contrib import admin
from .models import TipoAnuncio, Anuncio, Categoria

admin.site.register(TipoAnuncio)
admin.site.register(Anuncio)
admin.site.register(Categoria)
