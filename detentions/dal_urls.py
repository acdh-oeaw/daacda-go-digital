from django.conf.urls import url
from . import views
from . import dal_views
from .models import *

app_name = 'vocabs'

urlpatterns = [
    url(
        r'^prisonstationaltname-autocomplete/$', dal_views.PrisonStationAltNameAC.as_view(
            model=AlternativeName, create_field='name',),
        name='prisonstationaltname-autocomplete',
    ),
    url(
        r'^prisonstationlocatedinplace-autocomplete/$', dal_views.PrisonStationLocatedInPlaceAC.as_view(
            model=Place, create_field='name',),
        name='prisonstationlocatedinplace-autocomplete',
    ),
    url(
        r'^prisonstationpartof-autocomplete/$', dal_views.PrisonStationPartOfAC.as_view(
            model=Place, create_field='name',),
        name='prisonstationpartof-autocomplete',
    ),
    url(
        r'^prisonstationstationtype-autocomplete/$', dal_views.PrisonStationStationTypeAC.as_view(
            model=SkosConcept, create_field='pref_label',),
        name='prisonstationstationtype-autocomplete',
    ),
]
