from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .form import PlayerCreationForm, OwnerCreationForm


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
