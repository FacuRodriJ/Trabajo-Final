from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def no_login_required(function=None, redirect_field_name=None, login_url='index'):
    """
    Decorator for views that checks that the user is not logged in, redirecting
    to the index if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: not u.is_authenticated,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def owner_member_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME,
                          login_url='login'):
    """
    Decorador de vistas que comprueba que el usuario ha iniciado sesión y es miembro propietario, redirige a la página
    de inicio de sesión si es necesario.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_owner,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator
