import datetime
import time
import pandas as pd
import django_filters
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from browsing.models import BrowsConf
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_tables2 import SingleTableView, RequestConfig


from charts.models import ChartConfig
from charts.views import create_payload


def serialize(modelclass):
    """returns the field values of a model as list"""
    fields = modelclass._meta.get_fields()
    serialized = []
    for x in fields:
        if x.get_internal_type() == "ManyToManyField":
            attrs = getattr(modelclass, x.name)
            values = "|".join([y[1] for y in attrs.values_list()])
            key_value = values
        else:
            key_value = getattr(modelclass, x.name)
        serialized.append(key_value)
    return serialized


class GenericFilterFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(GenericFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.helper.form_tag = False
        self.add_input(Submit("Filter", "Search"))


django_filters.filters.LOOKUP_TYPES = [
    ("", "---------"),
    ("exact", "Is equal to"),
    ("iexact", "Is equal to (case insensitive)"),
    ("not_exact", "Is not equal to"),
    ("lt", "Lesser than/before"),
    ("gt", "Greater than/after"),
    ("gte", "Greater than or equal to"),
    ("lte", "Lesser than or equal to"),
    ("startswith", "Starts with"),
    ("endswith", "Ends with"),
    ("contains", "Contains"),
    ("icontains", "Contains (case insensitive)"),
    ("not_contains", "Does not contain"),
]


class GenericListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = "filter"
    paginate_by = 25
    template_name = "webpage/generic_list.html"

    def get_queryset(self, **kwargs):
        qs = super(GenericListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(
            self.request, paginate={"page": 1, "per_page": self.paginate_by}
        ).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        context["docstring"] = "{}".format(self.model.__doc__)
        if self.model.__name__.endswith("s"):
            context["class_name"] = "{}".format(self.model.__name__)
        else:
            context["class_name"] = "{}s".format(self.model.__name__)
        try:
            context["get_arche_dump"] = self.model.get_arche_dump()
        except AttributeError:
            context["get_arche_dump"] = None
        try:
            context["create_view_link"] = self.model.get_createview_url()
        except AttributeError:
            context["create_view_link"] = None
        try:
            context["dl_csv_link"] = self.model.dl_csv_link()
        except AttributeError:
            context["dl_csv_link"] = None

        model_name = self.model.__name__.lower()
        context["conf_items"] = list(
            BrowsConf.objects.filter(model_name=model_name).values_list(
                "field_path", "label"
            )
        )

        context["entity"] = model_name
        print(context["entity"])
        context["vis_list"] = ChartConfig.objects.filter(model_name=model_name)
        context["property_name"] = self.request.GET.get("property")
        context["charttype"] = self.request.GET.get("charttype")
        if context["charttype"] and context["property_name"]:
            qs = self.get_queryset()
            chartdata = create_payload(
                context["entity"], context["property_name"], context["charttype"], qs
            )
            context = dict(context, **chartdata)
            print(chartdata)
        return context

    def render_to_response(self, context, **kwargs):
        download = self.request.GET.get("sep", None)
        if download:
            sep = self.request.GET.get("sep", ",")
            timestamp = datetime.datetime.fromtimestamp(time.time()).strftime(
                "%Y-%m-%d-%H-%M-%S"
            )
            filename = "export_{}".format(timestamp)
            response = HttpResponse(content_type="text/csv")
            if context["conf_items"]:
                conf_items = context["conf_items"]
                try:
                    df = pd.DataFrame(
                        list(
                            self.model.objects.all().values_list(
                                *[x[0] for x in conf_items]
                            )
                        ),
                        columns=[x[1] for x in conf_items],
                    )
                except AssertionError:
                    response["Content-Disposition"] = (
                        'attachment; filename="{}.csv"'.format(filename)
                    )
                    return response
            else:
                response["Content-Disposition"] = (
                    'attachment; filename="{}.csv"'.format(filename)
                )
                return response
            if sep == "comma":
                df.to_csv(response, sep=",", index=False)
            elif sep == "semicolon":
                df.to_csv(response, sep=";", index=False)
            elif sep == "tab":
                df.to_csv(response, sep="\t", index=False)
            else:
                df.to_csv(response, sep=",", index=False)
            response["Content-Disposition"] = 'attachment; filename="{}.csv"'.format(
                filename
            )
            return response
        else:
            response = super(GenericListView, self).render_to_response(context)
            return response


class BaseCreateView(CreateView):
    model = None
    form_class = None
    template_name = "webpage/generic_create.html"

    def get_context_data(self, **kwargs):
        context = super(BaseCreateView, self).get_context_data()
        context["docstring"] = "{}".format(self.model.__doc__)
        if self.model.__name__.endswith("s"):
            context["class_name"] = "{}".format(self.model.__name__)
        else:
            context["class_name"] = "{}s".format(self.model.__name__)
        return context


class BaseUpdateView(UpdateView):
    model = None
    form_class = None
    template_name = "webpage/generic_create.html"

    def get_context_data(self, **kwargs):
        context = super(BaseUpdateView, self).get_context_data()
        context["docstring"] = "{}".format(self.model.__doc__)
        if self.model.__name__.endswith("s"):
            context["class_name"] = "{}".format(self.model.__name__)
        else:
            context["class_name"] = "{}s".format(self.model.__name__)
        return context
