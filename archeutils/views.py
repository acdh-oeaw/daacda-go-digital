from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, JsonResponse
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
    g = get_root_col()
    if format == 'turtle':
        return HttpResponse(
            g.serialize(encoding='utf-8', format='turtle'), content_type='text/turtle'
        )
    else:
        return HttpResponse(
            g.serialize(encoding='utf-8'), content_type='application/xml'
        )


def get_ids(request):
    base_uri = request.build_absolute_uri().split('/aschach')[0]
    data = {
        "arche_constants": f"{base_uri}{reverse('aschach:project_as_arche')}",
        "id_prefix": f"{ARCHE_BASE_URL}",
        "ids": [
            {
                "id": f"{get_arche_id(x)}",
                "filename": f"{slugify(x)}.xml",
                "md": f"{base_uri}{x.get_arche_url()}",
                "html": f"{base_uri}{x.get_absolute_url()}",
                "payload": f"{base_uri}{x.get_tei_url()}"
            } for x in Angabe.objects.all()[40000:40010]],
    }
    return JsonResponse(data)
