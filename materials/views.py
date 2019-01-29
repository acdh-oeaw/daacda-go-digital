from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django_tables2 import RequestConfig

from browsing.browsing_utils import BaseCreateView, BaseUpdateView, GenericListView

from . filters import UserContributionListFilter
from . forms import UserContributionForm, UserContributionFilterFormHelper
from . models import UserContribution
from . tables import UserContributionTable


class UserContributionListView(GenericListView):
    model = UserContribution
    table_class = UserContributionTable
    filter_class = UserContributionListFilter
    formhelper_class = UserContributionFilterFormHelper
    init_columns = [
        'id',
        'public',
    ]

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