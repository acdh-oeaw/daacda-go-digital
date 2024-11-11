from django.urls import path
from . import views, geojson_views, netviz_views


app_name = "entities"

urlpatterns = [
    path("altnames/", views.AlternativeNameListView.as_view(), name="browse_altnames"),
    path(
        "altnames/detail/<int:pk>",
        views.AlternativeNameDetailView.as_view(),
        name="alternativename_detail",
    ),
    path(
        "altnames/create/",
        views.AlternativeNameCreate.as_view(),
        name="alternativename_create",
    ),
    path(
        "altnames/edit/<int:pk>",
        views.AlternativeNameUpdate.as_view(),
        name="alternativename_edit",
    ),
    path(
        "altnames/delete/<int:pk>",
        views.AlternativeNameDelete.as_view(),
        name="alternativename_delete",
    ),
    path("places/", views.PlaceListView.as_view(), name="browse_places"),
    path(
        "crash-places/",
        views.CrashPlaceListView.as_view(),
        name="browse_crash_places",
    ),
    path(
        "crash-place-geojson/",
        geojson_views.crash_places_json,
        name="crash_places_geojson",
    ),
    path("place/create/", views.create_place, name="place_create"),
    path(
        "place/detail/<int:pk>",
        views.PlaceDetailView.as_view(),
        name="place_detail",
    ),
    path("place/edit/<int:pk>", views.edit_place, name="place_edit"),
    path(
        "place/delete/<int:pk>",
        views.PlaceDelete.as_view(),
        name="place_delete",
    ),
    path(
        "institutions/",
        views.InstitutionListView.as_view(),
        name="browse_institutions",
    ),
    path("bomb-group/", views.BombGroupListView.as_view(), name="browse_bombgroups"),
    path("airforces/", views.AirForceListView.as_view(), name="browse_airforces"),
    path("squads/", views.SquadListView.as_view(), name="browse_squads"),
    path(
        "institution/detail/<int:pk>",
        views.InstitutionDetailView.as_view(),
        name="institution_detail",
    ),
    path(
        "institution/netviz/<int:pk>",
        netviz_views.inst_planes_json,
        name="inst_planes_json",
    ),
    path(
        "institution/delete/<int:pk>",
        views.InstitutionDelete.as_view(),
        name="institution_delete",
    ),
    path(
        "institution/edit/<int:pk>",
        views.InstitutionUpdate.as_view(),
        name="institution_edit",
    ),
    path(
        "institution/create/",
        views.InstitutionCreate.as_view(),
        name="institution_create",
    ),
    path("persons/", views.PersonListView.as_view(), name="browse_persons"),
    path(
        "persons/detail/<int:pk>",
        views.PersonDetailView.as_view(),
        name="person_detail",
    ),
    path("person/create/", views.PersonCreate.as_view(), name="person_create"),
    path(
        "person/edit/<int:pk>",
        views.PersonUpdate.as_view(),
        name="person_edit",
    ),
    path(
        "person/delete/<int:pk>",
        views.PersonDelete.as_view(),
        name="person_delete",
    ),
    path("bombers/", views.BomberListView.as_view(), name="browse_bombers"),
    path("bomber-timestamps/", netviz_views.bomber_time_json, name="bomber_time_json"),
    path(
        "bombers/detail/<int:pk>",
        views.BomberDetailView.as_view(),
        name="bomber_detail",
    ),
    path("bomber/create/", views.BomberCreate.as_view(), name="bomber_create"),
    path(
        "bomber/edit/<int:pk>",
        views.BomberUpdate.as_view(),
        name="bomber_edit",
    ),
    path(
        "bomber/delete/<int:pk>",
        views.BomberDelete.as_view(),
        name="bomber_delete",
    ),
    path(
        "war-crime-cases/",
        views.WarCrimeCaseListView.as_view(),
        name="browse_warcrimecases",
    ),
    path(
        "war-crime-case/detail/<int:pk>",
        views.WarCrimeCaseDetailView.as_view(),
        name="warcrimecase_detail",
    ),
    path(
        "war-crime-case/create/",
        views.WarCrimeCaseCreate.as_view(),
        name="warcrimecase_create",
    ),
    path(
        "war-crime-case/edit/<int:pk>",
        views.WarCrimeCaseUpdate.as_view(),
        name="warcrimecase_edit",
    ),
    path(
        "war-crime-case/delete/<int:pk>",
        views.WarCrimeCaseDelete.as_view(),
        name="warcrimecase_delete",
    ),
    path("places-rdf/", views.PlaceRDFView.as_view(), name="rdf_places"),
    path("persons-rdf/", views.PersonRDFView.as_view(), name="rdf_persons"),
    path(
        "institutions-rdf/",
        views.InstitutionRDFView.as_view(),
        name="rdf_institutions",
    ),
    path("bombers/", views.BomberListView.as_view(), name="browse_bombers"),
    path(
        "onlineressources/",
        views.OnlineRessourceListView.as_view(),
        name="browse_onlineressources",
    ),
    path(
        "onlineressource/detail/<int:pk>",
        views.OnlineRessourceDetailView.as_view(),
        name="onlineressource_detail",
    ),
    path(
        "onlineressource/create/",
        views.OnlineRessourceCreate.as_view(),
        name="onlineressource_create",
    ),
    path(
        "onlineressource/edit/<int:pk>",
        views.OnlineRessourceUpdate.as_view(),
        name="onlineressource_edit",
    ),
    path(
        "onlineressource/delete/<int:pk>",
        views.OnlineRessourceDelete.as_view(),
        name="onlineressource_delete",
    ),
    path(
        "personwarcrimecases/",
        views.PersonWarCrimeCaseListView.as_view(),
        name="browse_personwarcrimecases",
    ),
    path(
        "personwarcrimecase/detail/<int:pk>",
        views.PersonWarCrimeCaseDetailView.as_view(),
        name="personwarcrimecase_detail",
    ),
    path(
        "personwarcrimecase/create/",
        views.PersonWarCrimeCaseCreate.as_view(),
        name="personwarcrimecase_create",
    ),
    path(
        "personwarcrimecase/edit/<int:pk>",
        views.PersonWarCrimeCaseUpdate.as_view(),
        name="personwarcrimecase_edit",
    ),
    path(
        "personwarcrimecase/delete/<int:pk>",
        views.PersonWarCrimeCaseDelete.as_view(),
        name="personwarcrimecase_delete",
    ),
    path(
        "airstrikes-geojson/",
        geojson_views.airstrikes_json,
        name="airstrikes_geojson",
    ),
    path(
        "airstrikes-timestamps/",
        netviz_views.airstrike_time_json,
        name="airstrike_time_json",
    ),
    path("airstrikes/", views.AirstrikeListView.as_view(), name="browse_airstrikes"),
    path(
        "airstrike/detail/<int:pk>",
        views.AirstrikeDetailView.as_view(),
        name="airstrike_detail",
    ),
    path(
        "airstrike/create/", views.AirstrikeCreate.as_view(), name="airstrike_create"
    ),
    path(
        "airstrike/edit/<int:pk>",
        views.AirstrikeUpdate.as_view(),
        name="airstrike_edit",
    ),
    path(
        "airstrike/delete/<int:pk>",
        views.AirstrikeDelete.as_view(),
        name="airstrike_delete",
    ),
]
