from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django_tables2 import RequestConfig

from browsing.browsing_utils import BaseCreateView, BaseUpdateView, GenericListView

from . filters import UserContributionListFilter, GedenkzeichenListFilter
from . forms import (
    UserContributionForm, UserContributionFilterFormHelper, GedenkzeichenForm,
    GedenkzeichenFilterFormHelper
)
from . models import UserContribution, Gedenkzeichen
from . tables import UserContributionTable, GedenkzeichenTable


class UserContributionListView(GenericListView):
    model = UserContribution
    table_class = UserContributionTable
    filter_class = UserContributionListFilter
    formhelper_class = UserContributionFilterFormHelper
    init_columns = [
        'id',
        'public',
    ]
    template_name = 'materials/usercontribution_list.html'


    def get_queryset(self, **kwargs):
        user = self.request.user
        qs = super(UserContributionListView, self).get_queryset()
        if user.is_authenticated:
            pass
        else:
            qs = qs.exclude(public=False)
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(UserContributionListView, self).get_context_data()
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


class UserContributionDetailView(DetailView):
    model = UserContribution
    template_name = 'materials/usercontribution_detail.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(UserContributionDetailView, self).get_context_data()
        if (self.object.public) or user.is_authenticated:
            pass
        else:
            context['not_logged_in'] = True
            return context
        return context


class UserContributionCreate(BaseCreateView):
    model = UserContribution
    form_class = UserContributionForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserContributionCreate, self).dispatch(*args, **kwargs)


class UserContributionUpdate(BaseUpdateView):
    model = UserContribution
    form_class = UserContributionForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserContributionUpdate, self).dispatch(*args, **kwargs)


class UserContributionDelete(DeleteView):
    model = UserContribution
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('materials:browse_usercontributions')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserContributionDelete, self).dispatch(*args, **kwargs)


class GedenkzeichenListView(GenericListView):
    model = Gedenkzeichen
    table_class = GedenkzeichenTable
    filter_class = GedenkzeichenListFilter
    formhelper_class = GedenkzeichenFilterFormHelper
    init_columns = [
        'id',
        'name',
    ]
    template_name = 'materials/gedenkzeichen_list.html'

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(GedenkzeichenListView, self).get_context_data()
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


class GedenkzeichenDetailView(DetailView):
    model = Gedenkzeichen
    template_name = 'materials/gedenkzeichen_detail.html'


class GedenkzeichenCreate(BaseCreateView):
    model = Gedenkzeichen
    form_class = GedenkzeichenForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GedenkzeichenCreate, self).dispatch(*args, **kwargs)


class GedenkzeichenUpdate(BaseUpdateView):
    model = Gedenkzeichen
    form_class = GedenkzeichenForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GedenkzeichenUpdate, self).dispatch(*args, **kwargs)


class GedenkzeichenDelete(DeleteView):
    model = Gedenkzeichen
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('materials:browse_gedenkzeichen')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GedenkzeichenDelete, self).dispatch(*args, **kwargs)
