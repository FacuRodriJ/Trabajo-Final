from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import views

from .views import PlayerSignUpView, OwnerSignUpView, CustomLoginView
from .decorators import no_login_required

urlpatterns = [
    path('login/', no_login_required(CustomLoginView.as_view()), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path("signup/", PlayerSignUpView.as_view(), name="player_signup"),
    path("signup/propietario/", staff_member_required(OwnerSignUpView.as_view()), name="owner_signup"),
    # Unicamente miembros de staff del proyecto pueden registrar un propietario.
]
