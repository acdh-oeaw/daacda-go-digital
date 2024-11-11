import json

from django.http import JsonResponse
from .models import Bomber, Airstrike


def crash_places_json(request):
    GEOJSON_STUMP = {"type": "FeatureCollection", "features": []}
    for x in Bomber.objects.exclude(crash_place__lng=None):
        GEOJSON_STUMP["features"].append(x.get_list_geojson())

    return JsonResponse(GEOJSON_STUMP)


def airstrikes_json(request):
    GEOJSON_STUMP = {"type": "FeatureCollection", "features": []}
    for x in Airstrike.objects.exclude(target__lng=None):
        GEOJSON_STUMP["features"].append(x.get_list_geojson())

    return JsonResponse(GEOJSON_STUMP)
