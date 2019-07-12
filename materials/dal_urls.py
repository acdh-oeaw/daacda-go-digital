from django.conf.urls import url
from . import views
from . import dal_views
from .models import *

app_name = 'vocabs'

urlpatterns = [
    url(
        r'^usercontributionperson-autocomplete/$',
        dal_views.UsercontributionPersonAC.as_view(model=Person, create_field='written_name',),
        name='usercontributionperson-autocomplete',
    ),
    url(
        r'^gedenkzeichenperson-autocomplete/$',
        dal_views.GedenkzeichenPersonAC.as_view(model=Person, create_field='written_name',),
        name='gedenkzeichenperson-autocomplete',
    ),
    url(
        r'^gedenkzeichenbomber-autocomplete/$',
        dal_views.GedenkzeichenBomberAC.as_view(model=Bomber, create_field='name',),
        name='gedenkzeichenbomber-autocomplete',
    ),
    url(
        r'^gedenkzeichenplace-autocomplete/$',
        dal_views.GedenkzeichenPlaceAC.as_view(model=Place, create_field='name',),
        name='gedenkzeichenplace-autocomplete',
    ),
]
