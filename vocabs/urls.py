from django.urls import re_path
from . import views

app_name = "vocabs"

urlpatterns = [
    re_path(r"^$", views.SkosConceptListView.as_view(), name="skosconcept_list"),
    re_path(
        r"^concepts/browse/$",
        views.SkosConceptFilterView.as_view(),
        name="browse_vocabs",
    ),
    re_path(
        r"^<int:pk>",
        views.SkosConceptDetailView.as_view(),
        name="skosconcept_detail",
    ),
    re_path(r"^create/$", views.SkosConceptCreate.as_view(), name="skosconcept_create"),
    re_path(
        r"^update/<int:pk>",
        views.SkosConceptUpdate.as_view(),
        name="skosconcept_update",
    ),
    re_path(
        r"^delete/<int:pk>",
        views.SkosConceptDelete.as_view(),
        name="skosconcept_delete",
    ),
    re_path(
        r"^scheme/$",
        views.SkosConceptSchemeListView.as_view(),
        name="skosconceptscheme_list",
    ),
    re_path(
        r"^scheme/<int:pk>",
        views.SkosConceptSchemeDetailView.as_view(),
        name="skosconceptscheme_detail",
    ),
    re_path(
        r"^scheme/create/$",
        views.SkosConceptSchemeCreate.as_view(),
        name="skosconceptscheme_create",
    ),
    re_path(
        r"^scheme/update/<int:pk>",
        views.SkosConceptSchemeUpdate.as_view(),
        name="skosconceptscheme_update",
    ),
    re_path(r"^label/$", views.SkosLabelListView.as_view(), name="skoslabel_list"),
    re_path(
        r"^label/<int:pk>",
        views.SkosLabelDetailView.as_view(),
        name="skoslabel_detail",
    ),
    re_path(
        r"^label/create/$", views.SkosLabelCreate.as_view(), name="skoslabel_create"
    ),
    re_path(
        r"^label/update/<int:pk>",
        views.SkosLabelUpdate.as_view(),
        name="skoslabel_update",
    ),
]
