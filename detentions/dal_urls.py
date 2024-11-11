from django.conf.urls import url
from . import views
from . import dal_views
from .models import *

app_name = "vocabs"

urlpatterns = [
    url(
        r"^prisonstationaltname-autocomplete/$",
        dal_views.PrisonStationAltNameAC.as_view(
            model=AlternativeName,
            create_field="name",
        ),
        name="prisonstationaltname-autocomplete",
    ),
    url(
        r"^prisonstationlocatedinplace-autocomplete/$",
        dal_views.PrisonStationLocatedInPlaceAC.as_view(
            model=Place,
            create_field="name",
        ),
        name="prisonstationlocatedinplace-autocomplete",
    ),
    url(
        r"^personprisonlocatedinplace-autocomplete/$",
        dal_views.PersonPrisonLocatedInPlaceAC.as_view(
            model=Place,
            create_field="name",
        ),
        name="personprisonlocatedinplace-autocomplete",
    ),
    url(
        r"^prisonstationpartof-autocomplete/$",
        dal_views.PrisonStationPartOfAC.as_view(
            model=Place,
            create_field="name",
        ),
        name="prisonstationpartof-autocomplete",
    ),
    url(
        r"^prisonstationstationtype-autocomplete/$",
        dal_views.PrisonStationStationTypeAC.as_view(
            model=SkosConcept,
            create_field="pref_label",
        ),
        name="prisonstationstationtype-autocomplete",
    ),
    url(
        r"^personprisonrelationtype-autocomplete/$",
        dal_views.PersonPrisonRelationTypeAC.as_view(
            model=SkosConcept,
            create_field="pref_label",
        ),
        name="personprisonrelationtype-autocomplete",
    ),
    url(
        r"^personprisonrelatedpersons-autocomplete/$",
        dal_views.PersonPrisonRelatedPersonsAC.as_view(
            model=Person,
            create_field="written_name",
        ),
        name="personprisonrelatedpersons-autocomplete",
    ),
    url(
        r"^personprisonrelatedprisonstation-autocomplete/$",
        dal_views.PersonPrisonRelatedPrisonStationAC.as_view(
            model=PrisonStation,
            create_field="name",
        ),
        name="personprisonrelatedprisonstation-autocomplete",
    ),
]
