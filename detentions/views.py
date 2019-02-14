from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from .models import PrisonStation, PersonPrison
from browsing.browsing_utils import BaseCreateView, BaseUpdateView, GenericListView
from .forms import PrisonStationForm, PersonPrisonForm
from detentions.filters import PrisonStationListFilter, PersonPrisonListFilter
from detentions.forms import PrisonStationFilterFormHelper, PersonPrisonFilterFormHelper
from detentions.tables import PrisonStationTable, PersonPrisonTable
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django_tables2 import RequestConfig


class PrisonStationListView(GenericListView):
    model = PrisonStation
    table_class = PrisonStationTable
    filter_class = PrisonStationListFilter
    formhelper_class = PrisonStationFilterFormHelper
    init_columns = [
        'name',
        'station_id',
        'located_in_place',
    ]
    enable_merge = True

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(PrisonStationListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
        return context

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by
        }).configure(table)
        default_cols = self.init_columns
        all_cols = self.get_all_cols()
        selected_cols = self.request.GET.getlist("columns") + default_cols
        exclude_vals = [x for x in all_cols if x not in selected_cols]
        table.exclude = exclude_vals
        return table


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


class PersonPrisonListView(GenericListView):
    model = PersonPrison
    table_class = PersonPrisonTable
    filter_class = PersonPrisonListFilter
    formhelper_class = PersonPrisonFilterFormHelper
    init_columns = [
        'id',
        'related_person',
        'relation_type',
        'related_prisonstation',
    ]

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(PersonPrisonListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
        return context

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by
        }).configure(table)
        default_cols = self.init_columns
        all_cols = self.get_all_cols()
        selected_cols = self.request.GET.getlist("columns") + default_cols
        exclude_vals = [x for x in all_cols if x not in selected_cols]
        table.exclude = exclude_vals
        return table


class PersonPrisonDetailView(DetailView):
    model = PersonPrison
    template_name = 'detentions/personprison_detail.html'


class PersonPrisonCreate(BaseCreateView):
    model = PersonPrison
    form_class = PersonPrisonForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonPrisonCreate, self).dispatch(*args, **kwargs)


class PersonPrisonUpdate(BaseUpdateView):
    model = PersonPrison
    form_class = PersonPrisonForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonPrisonUpdate, self).dispatch(*args, **kwargs)


class PersonPrisonDelete(DeleteView):
    model = PersonPrison
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('detentions:browse_personprisons')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonPrisonDelete, self).dispatch(*args, **kwargs)
