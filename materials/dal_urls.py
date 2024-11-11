from django.urls import path
from . import dal_views


app_name = "vocabs"

urlpatterns = [
    path(
        "usercontributionperson-autocomplete",
        dal_views.UsercontributionPersonAC.as_view(),
        name="usercontributionperson-autocomplete",
    ),
    path(
        "gedenkzeichenperson-autocomplete",
        dal_views.GedenkzeichenPersonAC.as_view(),
        name="gedenkzeichenperson-autocomplete",
    ),
    path(
        "gedenkzeichenbomber-autocomplete",
        dal_views.GedenkzeichenBomberAC.as_view(),
        name="gedenkzeichenbomber-autocomplete",
    ),
    path(
        "gedenkzeichenplace-autocomplete",
        dal_views.GedenkzeichenPlaceAC.as_view(),
        name="gedenkzeichenplace-autocomplete",
    ),
]
