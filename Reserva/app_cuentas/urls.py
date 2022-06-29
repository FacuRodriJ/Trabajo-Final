from django.urls import path

from .views import PlayerSignUpView, OwnerSignUpView
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path("signup/", PlayerSignUpView.as_view(), name="player_signup"),
    path("signup/propietario/", staff_member_required(OwnerSignUpView.as_view()), name="owner_signup"),
    # Unicamente miembros de staff del proyecto pueden registrar un propietario.
]