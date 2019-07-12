from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from entities.apis_views import PlaceViewSet, GeoJsonViewSet, AlternativNameViewSet

from vocabs import api_views

router = routers.DefaultRouter()
router.register(r'geojson', GeoJsonViewSet, base_name='places')
router.register(r'skoslabels', api_views.SkosLabelViewSet)
router.register(r'skosnamespaces', api_views.SkosNamespaceViewSet)
router.register(r'skosconceptschemes', api_views.SkosConceptSchemeViewSet)
router.register(r'skosconcepts', api_views.SkosConceptViewSet)
router.register(r'alt-names', AlternativNameViewSet)
router.register(r'places', PlaceViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^arche/', include('arche.urls', namespace='arche')),
    url(r'^browsing/', include('browsing.urls', namespace='browsing')),
    url(r'^charts/', include('charts.urls', namespace='charts')),
    url(r'^vocabs/', include('vocabs.urls', namespace='vocabs')),
    url(r'^vocabs-ac/', include('vocabs.dal_urls', namespace='vocabs-ac')),
    url(r'^entities-ac/', include('entities.dal_urls', namespace='entities-ac')),
    url(r'^entities/', include('entities.urls', namespace='entities')),
    url(r'^materials/', include('materials.urls', namespace='materials')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^detentions/', include('detentions.urls', namespace='detentions')),
    url(r'^detentions-ac/', include('detentions.dal_urls', namespace='detentions-ac')),
    url(r'^materials-ac/', include('materials.dal_urls', namespace='materials-ac')),
    url(r'^', include('webpage.urls', namespace='webpage')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
