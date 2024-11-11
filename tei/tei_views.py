from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, Http404

from .tei_utils import MakeTeiDoc


def res_as_tei(request, app_label, model_name, pk):

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
    mytei = MakeTeiDoc(res)
    return HttpResponse(mytei.as_tei_str(), content_type="text/xml")
