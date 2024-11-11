from django.urls import path
from . import views

app_name = "detentions"

urlpatterns = [
    path(
        "prisonstations/",
        views.PrisonStationListView.as_view(),
        name="browse_prisonstations",
    ),
    path(
        "prisonstation/detail/<int:pk>",
        views.PrisonStationDetailView.as_view(),
        name="prisonstation_detail",
    ),
    path(
        "prisonstation/create/",
        views.PrisonStationCreate.as_view(),
        name="prisonstation_create",
    ),
    path(
        "prisonstation/edit/<int:pk>",
        views.PrisonStationUpdate.as_view(),
        name="prisonstation_edit",
    ),
    path(
        "prisonstation/delete/<int:pk>",
        views.PrisonStationDelete.as_view(),
        name="prisonstation_delete",
    ),
    path(
        "personprisons/",
        views.PersonPrisonListView.as_view(),
        name="browse_personprisons",
    ),
    path(
        "personprison/detail/<int:pk>",
        views.PersonPrisonDetailView.as_view(),
        name="personprison_detail",
    ),
    path(
        "personprison/create/",
        views.PersonPrisonCreate.as_view(),
        name="personprison_create",
    ),
    path(
        "personprison/edit/<int:pk>",
        views.PersonPrisonUpdate.as_view(),
        name="personprison_edit",
    ),
    path(
        "personprison/delete/<int:pk>",
        views.PersonPrisonDelete.as_view(),
        name="personprison_delete",
    ),
]
