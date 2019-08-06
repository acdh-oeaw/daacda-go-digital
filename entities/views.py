import requests
import re
import json
import time
import datetime
from django.http import HttpResponse
from django.shortcuts import (render, render_to_response, get_object_or_404, redirect)
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django_tables2 import RequestConfig
from .models import (
    Place,
    AlternativeName,
    Institution,
    Person,
    Bomber,
    WarCrimeCase,
    OnlineRessource,
    PersonWarCrimeCase,
    Airstrike
)
from .forms import *
from .serializer_arche import *
from .tables import (
    PersonTable,
    InstitutionTable,
    PlaceTable,
    AlternativeNameTable,
    BomberTable,
    WarCrimeCaseTable,
    OnlineRessourceTable,
    PersonWarCrimeCaseTable,
    AirstrikeTable
)
from .filters import (
    PersonListFilter,
    InstitutionListFilter,
    PlaceListFilter,
    AlternativeNameListFilter,
    BomberListFilter,
    WarCrimeCaseListFilter,
    OnlineRessourceListFilter,
    PersonWarCrimeCaseListFilter,
    AirstrikeListFilter
)
from browsing.browsing_utils import GenericListView, BaseCreateView, BaseUpdateView

from . utils import bomb_group, crash_places, attack_places, airforce, squad
from . network_utils import flatten_graphs

from . models import NODE_TYPES


try:
    from browsing.models import BrowsConf
except ImportError:
    BrowsConf = None


class SquadListView(GenericListView):
    model = Institution
    table_class = InstitutionTable
    filter_class = InstitutionListFilter
    formhelper_class = InstitutionFilterFormHelper
    template_name = "entities/squad.html"
    init_columns = [
        'id',
        'written_name',
    ]

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(SquadListView, self).get_context_data()
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

    def get_queryset(self, **kwargs):
        self.filter = self.filter_class(self.request.GET, queryset=squad)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs


class AirForceListView(GenericListView):
    model = Institution
    table_class = InstitutionTable
    filter_class = InstitutionListFilter
    formhelper_class = InstitutionFilterFormHelper
    template_name = "entities/airforce.html"
    init_columns = [
        'id',
        'written_name',
    ]

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(AirForceListView, self).get_context_data()
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

    def get_queryset(self, **kwargs):
        self.filter = self.filter_class(self.request.GET, queryset=airforce)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs


class BombGroupListView(GenericListView):
    model = Institution
    table_class = InstitutionTable
    filter_class = InstitutionListFilter
    formhelper_class = InstitutionFilterFormHelper
    template_name = "entities/bomb_group.html"
    init_columns = [
        'id',
        'written_name',
    ]

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(BombGroupListView, self).get_context_data()
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

    def get_queryset(self, **kwargs):
        self.filter = self.filter_class(self.request.GET, queryset=bomb_group)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs


class InstitutionListView(GenericListView):
    model = Institution
    table_class = InstitutionTable
    filter_class = InstitutionListFilter
    formhelper_class = InstitutionFilterFormHelper
    init_columns = [
        'id',
        'written_name',
    ]

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(InstitutionListView, self).get_context_data()
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


class InstitutionRDFView(GenericListView):
    model = Institution
    table_class = InstitutionTable
    template_name = None
    filter_class = InstitutionListFilter
    formhelper_class = InstitutionFilterFormHelper

    def render_to_response(self, context):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
        response = HttpResponse(content_type='application/xml; charset=utf-8')
        filename = "institutions_{}".format(timestamp)
        response['Content-Disposition'] = 'attachment; filename="{}.rdf"'.format(filename)
        g = inst_to_arche(self.get_queryset())
        get_format = self.request.GET.get('format', default='n3')
        result = g.serialize(destination=response, format=get_format)
        return response


class InstitutionDetailView(DetailView):
    model = Institution
    template_name = 'entities/institution_detail.html'

    def get_context_data(self, **kwargs):
        context = super(InstitutionDetailView, self).get_context_data()
        bombers = self.object.has_bomber.all()
        graphs = []
        for x in bombers:
            graphs.append(x.netvis_data())
        graph = flatten_graphs(graphs)
        graph['nodes'].append(self.object.as_node())
        for x in bombers:
            graph['edges'].append(
                {
                    'id': f"{self.object.as_node()['id']}__{x.as_node()['id']}",
                    'source': self.object.as_node()['id'],
                    'target': x.as_node()['id'],
                    'label': 'hat Flugzeug'
                }
            )
        graph['types'] = {
            'nodes': NODE_TYPES
        }
        context['netvis_data'] = graph
        return context


class InstitutionCreate(BaseCreateView):

    model = Institution
    form_class = InstitutionForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InstitutionCreate, self).dispatch(*args, **kwargs)


class InstitutionUpdate(BaseUpdateView):

    model = Institution
    form_class = InstitutionForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InstitutionUpdate, self).dispatch(*args, **kwargs)


class InstitutionDelete(DeleteView):
    model = Institution
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('entities:browse_institutions')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InstitutionDelete, self).dispatch(*args, **kwargs)


class PersonListView(GenericListView):
    model = Person
    table_class = PersonTable
    filter_class = PersonListFilter
    formhelper_class = PersonFilterFormHelper
    init_columns = [
        'written_name', 'rank', 'destiny_checked',
    ]

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data()
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


class PersonRDFView(GenericListView):
    model = Person
    table_class = PersonTable
    template_name = None
    filter_class = PersonListFilter
    formhelper_class = PersonFilterFormHelper

    def render_to_response(self, context):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
        response = HttpResponse(content_type='application/xml; charset=utf-8')
        filename = "places_{}".format(timestamp)
        response['Content-Disposition'] = 'attachment; filename="{}.rdf"'.format(filename)
        g = person_to_arche(self.get_queryset())
        get_format = self.request.GET.get('format', default='n3')
        result = g.serialize(destination=response, format=get_format)
        return response


class PersonDetailView(DetailView):
    model = Person
    template_name = 'entities/person_detail.html'


class PersonCreate(BaseCreateView):

    model = Person
    form_class = PersonForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonCreate, self).dispatch(*args, **kwargs)


class PersonUpdate(BaseUpdateView):

    model = Person
    form_class = PersonForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonUpdate, self).dispatch(*args, **kwargs)


class PersonDelete(DeleteView):
    model = Person
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('entities:browse_persons')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonDelete, self).dispatch(*args, **kwargs)


class BomberListView(GenericListView):
    model = Bomber
    table_class = BomberTable
    filter_class = BomberListFilter
    formhelper_class = BomberFilterFormHelper
    init_columns = [
        'id', 'macr_nr', 'squadron', 'date_of_crash', 'crash_place', 'has_crew'
    ]

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(BomberListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
        gj_dicts = [
            x.get_list_geojson() for x in self.get_queryset()
            .filter(crash_place__lat__isnull=False)
        ]
        feature_collection = {
            'type': 'FeatureCollection',
            'features': gj_dicts
        }
        context['geojson'] = json.dumps(feature_collection)
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


class BomberDetailView(DetailView):
    model = Bomber
    template_name = 'entities/bomber_detail.html'


class BomberCreate(BaseCreateView):

    model = Bomber
    form_class = BomberForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BomberCreate, self).dispatch(*args, **kwargs)


class BomberUpdate(BaseUpdateView):

    model = Bomber
    form_class = BomberForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BomberUpdate, self).dispatch(*args, **kwargs)


class BomberDelete(DeleteView):
    model = Bomber
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('entities:browse_bombers')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BomberDelete, self).dispatch(*args, **kwargs)


class AlternativeNameListView(GenericListView):
    model = AlternativeName
    table_class = AlternativeNameTable
    filter_class = AlternativeNameListFilter
    formhelper_class = AlternativeNameFilterFormHelper
    init_columns = [
        'id',
        'name',
    ]

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(AlternativeNameListView, self).get_context_data()
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


class AlternativeNameDetailView(DetailView):
    model = AlternativeName
    template_name = 'entities/alternativenames_detail.html'


class AlternativeNameCreate(BaseCreateView):

    model = AlternativeName
    form_class = AlternativeNameForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AlternativeNameCreate, self).dispatch(*args, **kwargs)


class AlternativeNameUpdate(BaseUpdateView):

    model = AlternativeName
    form_class = AlternativeNameForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AlternativeNameUpdate, self).dispatch(*args, **kwargs)


class AlternativeNameDelete(DeleteView):
    model = AlternativeName
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('entities:browse_altnames')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AlternativeNameDelete, self).dispatch(*args, **kwargs)


class PlaceListView(GenericListView):
    model = Place
    table_class = PlaceTable
    filter_class = PlaceListFilter
    formhelper_class = PlaceFilterFormHelper
    init_columns = [
        'id',
        'name',
        'part_oc'
    ]

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(PlaceListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
        gj_dicts = [x.get_list_geojson() for x in self.get_queryset().filter(lat__isnull=False)]
        feature_collection = {
            'type': 'FeatureCollection',
            'features': gj_dicts
        }
        context['geojson'] = json.dumps(feature_collection)
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


class CrashPlaceListView(GenericListView):
    model = Place
    table_class = PlaceTable
    filter_class = PlaceListFilter
    formhelper_class = PlaceFilterFormHelper
    template_name = "entities/crash_place.html"
    init_columns = [
        'id',
        'name',
        'part_oc'
    ]

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(CrashPlaceListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
        gj_dicts = [x.get_list_geojson() for x in self.get_queryset().filter(lat__isnull=False)]
        feature_collection = {
            'type': 'FeatureCollection',
            'features': gj_dicts
        }
        context['geojson'] = json.dumps(feature_collection)
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

    def get_queryset(self, **kwargs):
        qs = super(CrashPlaceListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=crash_places)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs


class PlaceRDFView(GenericListView):
    model = Place
    table_class = PlaceTable
    template_name = None
    filter_class = PlaceListFilter
    formhelper_class = PlaceFilterFormHelper

    def render_to_response(self, context):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
        response = HttpResponse(content_type='application/xml; charset=utf-8')
        filename = "places_{}".format(timestamp)
        response['Content-Disposition'] = 'attachment; filename="{}.rdf"'.format(filename)
        g = place_to_arche(self.get_queryset())
        get_format = self.request.GET.get('format', default='n3')
        result = g.serialize(destination=response, format=get_format)
        return response


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'entities/place_detail.html'


@login_required
def create_place(request):
    if request.method == "POST":
        form = PlaceFormCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entities:browse_places')
        else:
            return render(request, 'entities/edit_places.html', {'form': form})
    else:
        form = PlaceFormCreate()
        return render(request, 'entities/edit_places.html', {'form': form})


@login_required
def edit_place(request, pk):
    instance = Place.objects.get(id=pk)
    username = "&username=digitalarchiv"
    if request.method == "GET":
        placeName = instance.name
        root = "http://api.geonames.org/searchJSON?q="
        params = "&fuzzy=0.6&lang=en&maxRows=100"
        url = root+placeName+params+username
        try:
            r = requests.get(url)
            response = r.text
            responseJSON = json.loads(response)
            responseJSON = responseJSON['geonames']
            form = PlaceForm(instance=instance)
            print(url)
            return render(
                request, 'entities/edit_places.html',
                {'object': instance, 'form': form, 'responseJSON': responseJSON}
            )
        except requests.exceptions.RequestException as e:
            url = e
        form = PlaceForm(instance=instance)

        responseJSON = "hansi"
        return render(
            request, 'entities/edit_places.html',
            {'object': instance, 'form': form, 'responseJSON': responseJSON}
        )
    else:
        form = PlaceForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return redirect('entities:browse_places')


class PlaceDelete(DeleteView):
    model = Place
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('entities:browse_places')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceDelete, self).dispatch(*args, **kwargs)


class WarCrimeCaseListView(GenericListView):
    model = WarCrimeCase
    table_class = WarCrimeCaseTable
    filter_class = WarCrimeCaseListFilter
    formhelper_class = WarCrimeCaseFilterFormHelper
    init_columns = [
        'id',
        'signatur',
        'warcrimespersons', 'warcrimesurls',
    ]

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(WarCrimeCaseListView, self).get_context_data()
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


class WarCrimeCaseDetailView(DetailView):
    model = WarCrimeCase
    template_name = 'entities/warcrimecase_detail.html'


class WarCrimeCaseCreate(BaseCreateView):
    model = WarCrimeCase
    form_class = WarCrimeCaseForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WarCrimeCaseCreate, self).dispatch(*args, **kwargs)


class WarCrimeCaseUpdate(BaseUpdateView):
    model = WarCrimeCase
    form_class = WarCrimeCaseForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WarCrimeCaseUpdate, self).dispatch(*args, **kwargs)


class WarCrimeCaseDelete(DeleteView):
    model = WarCrimeCase
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('entities:browse_warcrimecases')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WarCrimeCaseDelete, self).dispatch(*args, **kwargs)


class OnlineRessourceListView(GenericListView):
    model = OnlineRessource
    table_class = OnlineRessourceTable
    filter_class = OnlineRessourceListFilter
    formhelper_class = OnlineRessourceFilterFormHelper
    init_columns = [
        'www_url', 'onlineressourcepersons', 'onlineressourcebombers', 'onlineressourcewarcrimecases'
    ]

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(OnlineRessourceListView, self).get_context_data()
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


class OnlineRessourceDetailView(DetailView):
    model = OnlineRessource
    template_name = 'entities/onlineressource_detail.html'


class OnlineRessourceCreate(BaseCreateView):
    model = OnlineRessource
    form_class = OnlineRessourceForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OnlineRessourceCreate, self).dispatch(*args, **kwargs)


class OnlineRessourceUpdate(BaseUpdateView):
    model = OnlineRessource
    form_class = OnlineRessourceForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OnlineRessourceUpdate, self).dispatch(*args, **kwargs)


class OnlineRessourceDelete(DeleteView):
    model = OnlineRessource
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('entities:browse_onlineressources')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OnlineRessourceDelete, self).dispatch(*args, **kwargs)


class PersonWarCrimeCaseListView(GenericListView):
    model = PersonWarCrimeCase
    table_class = PersonWarCrimeCaseTable
    filter_class = PersonWarCrimeCaseListFilter
    formhelper_class = PersonWarCrimeCaseFilterFormHelper
    init_columns = [
        'id',
        'related_persons',
        'relation_type',
        'related_cases',
    ]

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(PersonWarCrimeCaseListView, self).get_context_data()
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


class PersonWarCrimeCaseDetailView(DetailView):
    model = PersonWarCrimeCase
    template_name = 'entities/personwarcrimecase_detail.html'


class PersonWarCrimeCaseCreate(BaseCreateView):
    model = PersonWarCrimeCase
    form_class = PersonWarCrimeCaseForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonWarCrimeCaseCreate, self).dispatch(*args, **kwargs)


class PersonWarCrimeCaseUpdate(BaseUpdateView):
    model = PersonWarCrimeCase
    form_class = PersonWarCrimeCaseForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonWarCrimeCaseUpdate, self).dispatch(*args, **kwargs)


class PersonWarCrimeCaseDelete(DeleteView):
    model = PersonWarCrimeCase
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('entities:browse_personwarcrimecases')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonWarCrimeCaseDelete, self).dispatch(*args, **kwargs)


class AirstrikeListView(GenericListView):
    model = Airstrike
    table_class = AirstrikeTable
    filter_class = AirstrikeListFilter
    formhelper_class = AirstrikeFilterFormHelper
    init_columns = [
        'date', 'target', 'country',
    ]

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(AirstrikeListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
        gj_dicts = [
            x.get_list_geojson() for x in self.get_queryset().filter(target__lat__isnull=False)
        ]
        feature_collection = {
            'type': 'FeatureCollection',
            'features': gj_dicts
        }
        context['geojson'] = json.dumps(feature_collection)
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


class AirstrikeRDFView(GenericListView):
    model = Airstrike
    table_class = AirstrikeTable
    template_name = None
    filter_class = AirstrikeListFilter
    formhelper_class = AirstrikeFilterFormHelper

    def render_to_response(self, context):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
        response = HttpResponse(content_type='application/xml; charset=utf-8')
        filename = "places_{}".format(timestamp)
        response['Content-Disposition'] = 'attachment; filename="{}.rdf"'.format(filename)
        g = person_to_arche(self.get_queryset())
        get_format = self.request.GET.get('format', default='n3')
        result = g.serialize(destination=response, format=get_format)
        return response


class AirstrikeDetailView(DetailView):
    model = Airstrike
    template_name = 'entities/airstrike_detail.html'


class AirstrikeCreate(BaseCreateView):

    model = Airstrike
    form_class = AirstrikeForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AirstrikeCreate, self).dispatch(*args, **kwargs)


class AirstrikeUpdate(BaseUpdateView):

    model = Airstrike
    form_class = AirstrikeForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AirstrikeUpdate, self).dispatch(*args, **kwargs)


class AirstrikeDelete(DeleteView):
    model = Airstrike
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('entities:browse_airstrikes')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AirstrikeDelete, self).dispatch(*args, **kwargs)
