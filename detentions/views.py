from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from .models import PrisonStation
from webpage.utils import BaseCreateView, BaseUpdateView
from .forms import PrisonStationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


class PrisonStationDetailView(DetailView):
    model = PrisonStation
    template_name = 'detentions/prisonstation_detail.html'


class PrisonStationCreate(BaseCreateView):
    model = PrisonStation
    form_class = PrisonStationForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PrisonStationCreate, self).dispatch(*args, **kwargs)


class PrisonStationUpdate(BaseUpdateView):
    model = PrisonStation
    form_class = PrisonStationForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PrisonStationUpdate, self).dispatch(*args, **kwargs)


class PrisonStationDelete(DeleteView):
    model = PrisonStation
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('detentions:browse_prisonstations')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PrisonStationDelete, self).dispatch(*args, **kwargs)
