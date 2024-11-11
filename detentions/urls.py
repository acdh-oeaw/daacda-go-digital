from django.conf.urls import url
from . import views

app_name = "detentions"

urlpatterns = [
    url(
        r"^prisonstations/$",
        views.PrisonStationListView.as_view(),
        name="browse_prisonstations",
    ),
    url(
        r"^prisonstation/detail/(?P<pk>[0-9]+)$",
        views.PrisonStationDetailView.as_view(),
        name="prisonstation_detail",
    ),
    url(
        r"^prisonstation/create/$",
        views.PrisonStationCreate.as_view(),
        name="prisonstation_create",
    ),
    url(
        r"^prisonstation/edit/(?P<pk>[0-9]+)$",
        views.PrisonStationUpdate.as_view(),
        name="prisonstation_edit",
    ),
    url(
        r"^prisonstation/delete/(?P<pk>[0-9]+)$",
        views.PrisonStationDelete.as_view(),
        name="prisonstation_delete",
    ),
    url(
        r"^personprisons/$",
        views.PersonPrisonListView.as_view(),
        name="browse_personprisons",
    ),
    url(
        r"^personprison/detail/(?P<pk>[0-9]+)$",
        views.PersonPrisonDetailView.as_view(),
        name="personprison_detail",
    ),
    url(
        r"^personprison/create/$",
        views.PersonPrisonCreate.as_view(),
        name="personprison_create",
    ),
    url(
        r"^personprison/edit/(?P<pk>[0-9]+)$",
        views.PersonPrisonUpdate.as_view(),
        name="personprison_edit",
    ),
    url(
        r"^personprison/delete/(?P<pk>[0-9]+)$",
        views.PersonPrisonDelete.as_view(),
        name="personprison_delete",
    ),
]
