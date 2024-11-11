from django.urls import path
from . import views

app_name = "materials"

urlpatterns = [
    path(
        "usercontributions/",
        views.UserContributionListView.as_view(),
        name="browse_usercontributions",
    ),
    path(
        "usercontribution/detail/<int:pk>",
        views.UserContributionDetailView.as_view(),
        name="usercontribution_detail",
    ),
    path(
        "usercontribution/create/",
        views.UserContributionCreate.as_view(),
        name="usercontribution_create",
    ),
    path(
        "usercontribution/edit/<int:pk>",
        views.UserContributionUpdate.as_view(),
        name="usercontribution_edit",
    ),
    path(
        "usercontribution/delete/<int:pk>",
        views.UserContributionDelete.as_view(),
        name="usercontribution_delete",
    ),
    path(
        "gedenkzeichen/",
        views.GedenkzeichenListView.as_view(),
        name="browse_gedenkzeichen",
    ),
    path(
        "gedenkzeichen/detail/<int:pk>",
        views.GedenkzeichenDetailView.as_view(),
        name="gedenkzeichen_detail",
    ),
    path(
        "gedenkzeichen/create/",
        views.GedenkzeichenCreate.as_view(),
        name="gedenkzeichen_create",
    ),
    path(
        "gedenkzeichen/edit/<int:pk>",
        views.GedenkzeichenUpdate.as_view(),
        name="gedenkzeichen_edit",
    ),
    path(
        "gedenkzeichen/delete/<int:pk>",
        views.GedenkzeichenDelete.as_view(),
        name="gedenkzeichen_delete",
    ),
]
