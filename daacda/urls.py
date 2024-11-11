from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from entities.apis_views import PlaceViewSet, GeoJsonViewSet, AlternativNameViewSet

from vocabs import api_views

router = routers.DefaultRouter()
router.register(r"geojson", GeoJsonViewSet, basename="places")
router.register(r"skoslabels", api_views.SkosLabelViewSet)
router.register(r"skosnamespaces", api_views.SkosNamespaceViewSet)
router.register(r"skosconceptschemes", api_views.SkosConceptSchemeViewSet)
router.register(r"skosconcepts", api_views.SkosConceptViewSet)
router.register(r"alt-names", AlternativNameViewSet)
router.register(r"places", PlaceViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
    path("browsing/", include("browsing.urls", namespace="browsing")),
    path("vocabs/", include("vocabs.urls", namespace="vocabs")),
    path("vocabs-ac/", include("vocabs.dal_urls", namespace="vocabs-ac")),
    path("entities-ac/", include("entities.dal_urls", namespace="entities-ac")),
    path("entities/", include("entities.urls", namespace="entities")),
    path("materials/", include("materials.urls", namespace="materials")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("detentions/", include("detentions.urls", namespace="detentions")),
    path("detentions-ac/", include("detentions.dal_urls", namespace="detentions-ac")),
    path("materials-ac/", include("materials.dal_urls", namespace="materials-ac")),
    path("", include("webpage.urls", namespace="webpage")),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
