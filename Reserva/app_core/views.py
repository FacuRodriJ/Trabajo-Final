from django.contrib.auth.decorators import login_required
from django.views.generic.detail import SingleObjectMixin, DetailView
from django.views.generic import UpdateView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, QueryDict
from django.urls import reverse_lazy, reverse

from app_cuentas.models import Propietario, Usuario
from .models import Establecimiento


class ProfileObjectMixin(SingleObjectMixin):
    """
    Provides views with the current user's profile.
    """
    model = Usuario

    # def get_object(self, queryset=None):
    #    """Return's the current users profile."""
    #    try:
    #        return self.request.user.get_profile()
    #    except Profile.DoesNotExist:
    #        raise NotImplemented(
    #            "What if the user doesn't have an associated profile?")

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """Ensures that only authenticated users can access the view."""
        if self.request.user.id == kwargs.get("pk"):
            return super(ProfileObjectMixin, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('select-establ', args=[self.request.user.id]))


class SelectEstablView(ProfileObjectMixin, DetailView):
    template_name = 'propietario/select-establ.html'

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            context['object'] = self.object
            context['establecimientos'] = Establecimiento.objects.filter(propietario__user_id=self.request.user.id)
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super().get_context_data(**context)
