"""projeto_integrador_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import AutenticandoUsuarioForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/accounts/login', permanent=True)),
    path('classificados-na-web/', include('classificados_na_web.urls'))
]

# Use static() to add url mapping to serve static files during development (only)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [
    path("accounts/login/", auth_view.LoginView.as_view(authentication_form=AutenticandoUsuarioForm), name="login"),
    path("accounts/logout/", auth_view.LogoutView.as_view(), name="logout"),
    path("accounts/password_change/", auth_view.PasswordChangeView.as_view(), name="password_change"),
    path("accounts/password_change/done/", auth_view.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("accounts/password_reset/", auth_view.PasswordResetView.as_view(), name="password_reset"),
    path("accounts/password_reset/done/", auth_view.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("accounts/reset/<uidb64>/<token>/", auth_view.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("accounts/reset/done/", auth_view.PasswordResetCompleteView.as_view(), name="password_reset_complete")]
