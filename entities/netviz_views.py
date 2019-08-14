import collections
import json

from django.http import JsonResponse
from . models import Airstrike, Institution, Bomber, NODE_TYPES
from . network_utils import flatten_graphs


def inst_planes_json(request, pk):
    current_object = Institution.objects.get(id=pk)
    if current_object.children_institutions.all()\
            .count() > 0 and current_object.parent_institution:
        bombers = Bomber.objects.filter(
            squadron__parent_institution=current_object
        )
    elif current_object.children_institutions.all().count():
        bombers = Bomber.objects.filter(
            squadron__parent_institution__parent_institution=current_object
        )
    else:
        bombers = current_object.has_bomber.all()

    graphs = []
    for x in bombers:
        graphs.append(x.netvis_data())
    graph = flatten_graphs(graphs)
    graph['nodes'].append(current_object.as_node())
    graph['types'] = {
        'nodes': NODE_TYPES
    }
    return JsonResponse(graph)


def airstrike_time_json(request):
    my_data = collections.Counter([x.crash_date_data() for x in Airstrike.objects.all()])
    return JsonResponse(my_data)
