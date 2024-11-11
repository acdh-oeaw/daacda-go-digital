from django.urls import path
from detentions import dal_views
from detentions.models import PrisonStation
from entities.models import Place, AlternativeName, Person
from vocabs.models import SkosConcept

app_name = "vocabs"

urlpatterns = [
    path(
        "prisonstationaltname-autocomplete/",
        dal_views.PrisonStationAltNameAC.as_view(
            model=AlternativeName,
            create_field="name",
        ),
        name="prisonstationaltname-autocomplete",
    ),
    path(
        "prisonstationlocatedinplace-autocomplete/",
        dal_views.PrisonStationLocatedInPlaceAC.as_view(
            model=Place,
            create_field="name",
        ),
        name="prisonstationlocatedinplace-autocomplete",
    ),
    path(
        "personprisonlocatedinplace-autocomplete/",
        dal_views.PersonPrisonLocatedInPlaceAC.as_view(
            model=Place,
            create_field="name",
        ),
        name="personprisonlocatedinplace-autocomplete",
    ),
    path(
        "prisonstationpartof-autocomplete/",
        dal_views.PrisonStationPartOfAC.as_view(
            model=Place,
            create_field="name",
        ),
        name="prisonstationpartof-autocomplete",
    ),
    path(
        "prisonstationstationtype-autocomplete/",
        dal_views.PrisonStationStationTypeAC.as_view(
            model=SkosConcept,
            create_field="pref_label",
        ),
        name="prisonstationstationtype-autocomplete",
    ),
    path(
        "personprisonrelationtype-autocomplete/",
        dal_views.PersonPrisonRelationTypeAC.as_view(
            model=SkosConcept,
            create_field="pref_label",
        ),
        name="personprisonrelationtype-autocomplete",
    ),
    path(
        "personprisonrelatedpersons-autocomplete/",
        dal_views.PersonPrisonRelatedPersonsAC.as_view(
            model=Person,
            create_field="written_name",
        ),
        name="personprisonrelatedpersons-autocomplete",
    ),
    path(
        "personprisonrelatedprisonstation-autocomplete/",
        dal_views.PersonPrisonRelatedPrisonStationAC.as_view(
            model=PrisonStation,
            create_field="name",
        ),
        name="personprisonrelatedprisonstation-autocomplete",
    ),
]
