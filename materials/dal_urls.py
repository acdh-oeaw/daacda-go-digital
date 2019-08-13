from django.conf.urls import url
from . import views
from . import dal_views
from .models import *

app_name = 'vocabs'

urlpatterns = [
    url(
        r'^usercontributionperson-autocomplete/$',
        dal_views.UsercontributionPersonAC.as_view(),
        name='usercontributionperson-autocomplete',
    ),
    url(
        r'^gedenkzeichenperson-autocomplete/$',
        dal_views.GedenkzeichenPersonAC.as_view(),
        name='gedenkzeichenperson-autocomplete',
    ),
    url(
        r'^gedenkzeichenbomber-autocomplete/$',
        dal_views.GedenkzeichenBomberAC.as_view(),
        name='gedenkzeichenbomber-autocomplete',
    ),
    url(
        r'^gedenkzeichenplace-autocomplete/$',
        dal_views.GedenkzeichenPlaceAC.as_view(),
        name='gedenkzeichenplace-autocomplete',
    ),
]
