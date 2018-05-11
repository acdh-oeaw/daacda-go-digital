from django.conf.urls import url
from . import views
from . import dal_views
from .models import *

app_name = 'vocabs'

urlpatterns = [
    url(
        r'^altname-autocomplete/$', dal_views.AlternativeNameAC.as_view(
            model=AlternativeName, create_field='name',),
        name='altname-autocomplete',
    ),
    url(
        r'^place-autocomplete/$', dal_views.PlaceAC.as_view(
            model=Place, create_field='name',),
        name='place-autocomplete',
    ),
    url(
        r'^person-autocomplete/$', dal_views.PersonAC.as_view(
            model=Place, create_field='name',),
        name='person-autocomplete',
    ),
    url(
        r'^institution-autocomplete/$', dal_views.InstitutionAC.as_view(
            model=Institution, create_field='written_name',),
        name='institution-autocomplete',
    ),
    url(
        r'^bomberplanetype-autocomplete/$', dal_views.BomberPlaneTypeAC.as_view(
            model=SkosConcept, create_field='pref_label',),
        name='bomberplanetype-autocomplete',
    ),
    url(
        r'^bombersquadron-autocomplete/$', dal_views.BomberSquadronAC.as_view(
            model=Institution, create_field='written_name',),
        name='bombersquadron-autocomplete',
    ),
    url(
        r'^bomberreasonofcrash-autocomplete/$', dal_views.BomberReasonOfCrashAC.as_view(
            model=SkosConcept, create_field='pref_label',),
        name='bomberreasonofcrash-autocomplete',
    ),
]
