from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.urls import reverse

from .utils import as_arche_graph, get_root_col, ARCHE_BASE_URL, get_arche_id


def res_as_arche_graph(request, app_label, model_name, pk):
    format = request.GET.get('format', 'xml')
    try:
        ct = ContentType.objects.get(app_label=app_label, model=model_name)
    except ObjectDoesNotExist:
        raise Http404(f"No model: {model_name} in app: {app_label} defined")
    try:
        int_pk = int(pk)
    except ValueError:
        raise Http404(f"No model: {model_name} with id: {pk} found")
    try:
        res = ct.model_class().objects.get(id=int_pk)
    except ObjectDoesNotExist:
        raise Http404(f"No model: {model_name} with id: {pk} found")
    g = as_arche_graph(res)
    if format == 'turtle':
        return HttpResponse(
            g.serialize(encoding='utf-8', format='turtle'), content_type='text/turtle'
        )
    else:
        return HttpResponse(
            g.serialize(encoding='utf-8'), content_type='application/xml'
        )


def top_col_md(request):
    format = request.GET.get('format', 'xml')
    g = get_root_col()
    if format == 'turtle':
        return HttpResponse(
            g.serialize(encoding='utf-8', format='turtle'), content_type='text/turtle'
        )
    else:
        return HttpResponse(
            g.serialize(encoding='utf-8'), content_type='application/xml'
        )


def get_ids(request, app_label, model_name):
    start = request.GET.get('start', 0)
    limit = request.GET.get('limit', False)
    print(limit)
    try:
        ct = ContentType.objects.get(app_label=app_label, model=model_name)
    except ObjectDoesNotExist:
        raise Http404(f"No model: {model_name} in app: {app_label} defined")
    curr_class = ct.model_class()
    if limit:
        try:
            final_limit = int(limit)
        except ValueError:
            final_limit = 10
    else:
        final_limit = curr_class.objects.all().count()
    print(limit)
    base_uri = request.build_absolute_uri().split('/archeutils')[0]
    # base_uri = "https://hansi4ever/"
    data = {
        "arche_constants": f"{base_uri}{reverse('archeutils:top_col_md')}",
        "id_prefix": f"{ARCHE_BASE_URL}",
        "ids": [
            {
                "id": f"{ARCHE_BASE_URL}/bomber__{x.id}.xml",
                "filename": f"bomber__{x.id}.xml",
                "md": f"{base_uri}/archeutils/md-resource/{app_label}/{model_name}/{x.id}",
                "html": f"{base_uri}{x.get_absolute_url()}",
                "payload": f"{base_uri}/tei/resource-as-tei/{app_label}/{model_name}/{x.id}",
                "mimetype": "application/xml"
            } for x in curr_class.objects.all()[0:final_limit]],
    }
    return JsonResponse(data)
