from django.conf.urls import url
from django.urls import path
from . import views
from . import dal_views
from .models import *

app_name = 'vocabs'

urlpatterns = [
    url(
        r'^altname-autocomplete/$', dal_views.AlternativeNameAC.as_view(
            model=AlternativeName,),
        name='altname-autocomplete',
    ),
    url(
        r'^place-autocomplete/$', dal_views.PlaceAC.as_view(
            model=Place,),
        name='place-autocomplete',
    ),
    url(
        r'^crash-place-autocomplete/$', dal_views.CrashPlaceAC.as_view(
            model=Place,),
        name='crash-place-autocomplete',
    ),
    url(
        r'^search-place-autocomplete/$', dal_views.PlaceAC.as_view(),
        name='search-place-autocomplete',
    ),
    url(
        r'^search-region-autocomplete/$', dal_views.Region.as_view(),
        name='search-region-autocomplete',
    ),
    url(
        r'^person-autocomplete/$', dal_views.PersonAC.as_view(
            model=Place,),
        name='person-autocomplete',
    ),
    url(
        r'^institution-autocomplete/$', dal_views.InstitutionAC.as_view(
            model=Institution,),
        name='institution-autocomplete',
    ),
    url(
        r'^bomberplanetype-autocomplete/$', dal_views.BomberPlaneTypeAC.as_view(
            model=SkosConcept),
        name='bomberplanetype-autocomplete',
    ),
    url(
        r'^bombersquadron-autocomplete/$', dal_views.BomberSquadronAC.as_view(
            model=Institution,),
        name='bombersquadron-autocomplete',
    ),
    url(
        r'^bomberreasonofcrash-autocomplete/$', dal_views.BomberReasonOfCrashAC.as_view(
            model=SkosConcept),
        name='bomberreasonofcrash-autocomplete',
    ),
    url(
        r'^personpartofbomber-autocomplete/$', dal_views.PersonPartOfBomberAC.as_view(
            model=Bomber),
        name='personpartofbomber-autocomplete',
    ),
    url(
        r'^personrank-autocomplete/$', dal_views.PersonRankAC.as_view(
            model=SkosConcept),
        name='personrank-autocomplete',
    ),
    url(
        r'^persondestinystated-autocomplete/$', dal_views.PersonDestinyStatedAC.as_view(
            model=SkosConcept),
        name='persondestinystated-autocomplete',
    ),
    url(
        r'^persondestinychecked-autocomplete/$', dal_views.PersonDestinyCheckedAC.as_view(
            model=SkosConcept),
        name='persondestinychecked-autocomplete',
    ),
    url(
        r'^personmia-autocomplete/$', dal_views.PersonMIAAC.as_view(
            model=SkosConcept),
        name='personmia-autocomplete',
    ),
    url(
        r'^onlineressourcerelatedpersons-autocomplete/$', dal_views.OnlineRessourceRelatedPersonsAC.as_view(
            model=Person,),
        name='onlineressourcerelatedpersons-autocomplete',
    ),
    url(
        r'^onlineressourcerelatedbombers-autocomplete/$', dal_views.OnlineRessourceRelatedBombersAC.as_view(
            model=Bomber,),
        name='onlineressourcerelatedbombers-autocomplete',
    ),
    url(
        r'^onlineressourcerelatedwarcrimecases-autocomplete/$', dal_views.OnlineRessourceRelatedWarCrimeCasesAC.as_view(
            model=WarCrimeCase,),
        name='onlineressourcerelatedwarcrimecases-autocomplete',
    ),
    url(
        r'^personwarcrimecaserelatedpersons-autocomplete/$', dal_views.PersonWarCrimeCaseRelatedPersonsAC.as_view(
            model=Person,),
        name='personwarcrimecaserelatedpersons-autocomplete',
    ),
    url(
        r'^personwarcrimecaserelatedcases-autocomplete/$', dal_views.PersonWarCrimeCaseRelatedCasesAC.as_view(
            model=WarCrimeCase,),
        name='personwarcrimecaserelatedcases-autocomplete',
    ),
    url(
        r'^personwarcrimecaserelationtype-autocomplete/$', dal_views.PersonWarCrimeCaseRelationTypeAC.as_view(
            model=SkosConcept),
        name='personwarcrimecaserelationtype-autocomplete',
    ),
    url(
        r'^warcrimecaserelatedpersons-autocomplete/$', dal_views.WarCrimeCaseRelatedPersonsAC.as_view(
            model=Person,),
        name='warcrimecaserelatedpersons-autocomplete',
    ),
    url(
        r'^warcrimecaserelatedcases-autocomplete/$', dal_views.WarCrimeCaseRelatedCasesAC.as_view(
            model=WarCrimeCase,),
        name='warcrimecaserelatedcases-autocomplete',
    ),
    url(
        r'^warcrimecaserelatedplaces-autocomplete/$', dal_views.WarCrimeCaseRelatedPlacesAC.as_view(
            model=Place,),
        name='warcrimecaserelatedplaces-autocomplete',
    ),
    url(
        r'^warcrimecasecrimetype-autocomplete/$', dal_views.WarCrimeCaseCrimeTypeAC.as_view(
            model=SkosConcept),
        name='warcrimecasecrimetype-autocomplete',
    ),
    url(
        r'^airstriketarget-autocomplete/$', dal_views.AirstrikeTargetAC.as_view(
            model=Place),
        name='airstriketarget-autocomplete',
    ),
    url(
        r'^airstrikeplanetype-autocomplete/$', dal_views.AirstrikePlaneTypeAC.as_view(
            model=SkosConcept),
        name='airstrikeplanetype-autocomplete',
    ),
    url(
        r'^airstrikeairforce-autocomplete/$', dal_views.AirstrikeAirforceAC.as_view(
            model=Institution,),
        name='airstrikeairforce-autocomplete',
    ),
    path(
        r'specific-place-ac/<str:lookup>', dal_views.PlaceConstraintAC.as_view(
            model=Place),
        name='specific-place-ac',
    ),
    path(
        r'specific-person-ac/<str:lookup>', dal_views.PersonConstraintAC.as_view(
            model=Place),
        name='specific-person-ac',
    )
]
