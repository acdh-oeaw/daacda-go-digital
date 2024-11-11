from django.urls import include, path
from . import tei_views

app_name = "tei"

urlpatterns = [
    path(
        "resource-as-tei/<app_label>/<model_name>/<pk>",
        tei_views.res_as_tei,
        name="res_as_tei",
    ),
]
