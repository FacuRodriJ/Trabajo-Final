from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import LoginView
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.http import HttpResponseRedirect, QueryDict

from .form import PlayerCreationForm, OwnerCreationForm


class CustomLoginView(LoginView):
    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        if self.request.user.is_owner:
            return HttpResponseRedirect(reverse('app_core:select-establ', args=[self.request.user.id]))
        else:
            return HttpResponseRedirect(self.get_success_url())


class PlayerSignUpView(CreateView):
    """
    Vista para la creación de un nuevo jugador.
    """
    form_class = PlayerCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class OwnerSignUpView(CreateView):
    """
    Vista para la creación de un nuevo propietario.
    """
    form_class = OwnerCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
