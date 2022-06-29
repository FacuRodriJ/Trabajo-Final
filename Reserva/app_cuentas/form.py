from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    password_validation,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Usuario


class PlayerCreationForm(forms.ModelForm):
    """
    Un formulario que crea un usuario sin privilegios, con los datos de email,
    dni, nombre completo y contraseña brindados. Se usa para generar jugadores.
    """
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Contraseña'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Confirmar contraseña'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = Usuario
        fields = ("email", "dni", "complete_name")
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email',
                    'autocomplete': 'off'
                }
            ),
            'dni': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'DNI',
                    'autocomplete': 'off'
                }
            ),
            'complete_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre completo',
                    'autocomplete': 'off'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class OwnerCreationForm(forms.ModelForm):
    """
    Un formulario que crea un usuario propietario de uno o más app_establecimientos,
    con los datos de email, dni, nombre completo, brindados.
    """
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Contraseña'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Confirmar contraseña'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = Usuario
        fields = ("email", "dni", "complete_name", "is_owner")
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email',
                    'autocomplete': 'off'
                }
            ),
            'dni': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'DNI',
                    'autocomplete': 'off'
                }
            ),
            'complete_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre completo',
                    'autocomplete': 'off'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True
        self.fields['is_owner'].initial = True
        # Establece el campo "is_owner" en el formulario como True.
        self.fields['is_owner'].widget = forms.HiddenInput()
        # Oculta el campo "is_owner" en el formulario para no cambiarlo a False por error.

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
