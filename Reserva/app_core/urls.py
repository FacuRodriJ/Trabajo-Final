from django.urls import path
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect, QueryDict
from django.urls import reverse_lazy, reverse



from app_cuentas.decorators import owner_member_required
from .views import SelectEstablView

app_name = 'app_core'
urlpatterns = [
    path('propietario/<int:pk>/',
         owner_member_required(TemplateView.as_view(template_name='propietario/dashboard.html')),
         name='owner-dashboard'),
    path('propietario/<int:pk>/select-establ', owner_member_required(SelectEstablView.as_view()), name='select-establ'),
]
