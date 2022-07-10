from django.utils import timezone
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail

from app_core.models import Establecimiento
from .apps import CuentasConfig


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_player', False)
        extra_fields.setdefault('is_owner', False)
        # El superusuario no es Jugador ni Propietario, ya que
        # no tendrá asignado una reserva o un establecimiento.

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Usuario(AbstractUser):
    """ Database model for users in the system """
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(_('email address'), unique=True)
    cuit = models.CharField(verbose_name='CUIT', max_length=150, unique=True)
    complete_name = models.CharField(_('complete name'), max_length=150)
    is_player = models.BooleanField(
        _('is player'),
        default=True,
        help_text=_('Designates the user is player.'))
    is_owner = models.BooleanField(
        _('is owner'),
        default=False,
        help_text=_('Designates the user is an establishment owner.'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cuit', 'complete_name']

    objects = CustomUserManager()

    class Meta:
        db_table = CuentasConfig.name + "_" + "usuario"

    def __str__(self):
        """ Return string representation of our user """
        return self.complete_name


class Jugador(models.Model):
    user = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name='jugador')

    class Meta:
        db_table = CuentasConfig.name + "_" + "jugador"


class Propietario(models.Model):
    user = models.OneToOneField(
        Usuario,
        on_delete=models.PROTECT,
        related_name='propietario')
    establ_en_uso = models.OneToOneField(
        Establecimiento,
        null=True,
        on_delete=models.PROTECT,
        related_name='establ_en_uso'
    )

    class Meta:
        db_table = CuentasConfig.name + "_" + "propietario"


@receiver(post_save, sender=Usuario)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.is_player:
        Jugador.objects.get_or_create(user=instance)
    if instance.is_owner:
        Propietario.objects.get_or_create(user=instance)


@receiver(post_save, sender=Usuario)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_player:
        instance.jugador.save()
    if instance.is_owner:
        instance.propietario.save()
