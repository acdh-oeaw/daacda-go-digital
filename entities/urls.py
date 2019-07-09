from django.conf.urls import url
from . import views

app_name = 'entities'

urlpatterns = [
    url(r'^altnames/$', views.AlternativeNameListView.as_view(), name='browse_altnames'),
    url(r'^altnames/detail/(?P<pk>[0-9]+)$', views.AlternativeNameDetailView.as_view(),
        name='alternativename_detail'),
    url(r'^altnames/create/$', views.AlternativeNameCreate.as_view(),
        name='alternativename_create'),
    url(r'^altnames/edit/(?P<pk>[0-9]+)$', views.AlternativeNameUpdate.as_view(),
        name='alternativename_edit'),
    url(r'^altnames/delete/(?P<pk>[0-9]+)$', views.AlternativeNameDelete.as_view(),
        name='alternativename_delete'),
    url(r'^places/$', views.PlaceListView.as_view(), name='browse_places'),
    url(r'^place/create/$', views.create_place, name='place_create'),
    url(r'^place/detail/(?P<pk>[0-9]+)$', views.PlaceDetailView.as_view(), name='place_detail'),
    url(r'^place/edit/(?P<pk>[0-9]+)$', views.edit_place, name='place_edit'),
    url(r'^place/delete/(?P<pk>[0-9]+)$', views.PlaceDelete.as_view(), name='place_delete'),
    url(r'^institutions/$', views.InstitutionListView.as_view(), name='browse_institutions'),
    url(r'^bomb-group/$', views.BombGroupListView.as_view(), name='browse_bombgroups'),
    url(r'^institution/detail/(?P<pk>[0-9]+)$', views.InstitutionDetailView.as_view(),
        name='institution_detail'),
    url(r'^institution/delete/(?P<pk>[0-9]+)$', views.InstitutionDelete.as_view(),
        name='institution_delete'),
    url(r'^institution/edit/(?P<pk>[0-9]+)$', views.InstitutionUpdate.as_view(),
        name='institution_edit'),
    url(r'^institution/create/$', views.InstitutionCreate.as_view(),
        name='institution_create'),
    url(r'^persons/$', views.PersonListView.as_view(), name='browse_persons'),
    url(r'^persons/detail/(?P<pk>[0-9]+)$', views.PersonDetailView.as_view(),
        name='person_detail'),
    url(r'^person/create/$', views.PersonCreate.as_view(),
        name='person_create'),
    url(r'^person/edit/(?P<pk>[0-9]+)$', views.PersonUpdate.as_view(),
        name='person_edit'),
    url(r'^person/delete/(?P<pk>[0-9]+)$', views.PersonDelete.as_view(),
        name='person_delete'),
    url(r'^bombers/$', views.BomberListView.as_view(), name='browse_bombers'),
    url(r'^bombers/detail/(?P<pk>[0-9]+)$', views.BomberDetailView.as_view(),
        name='bomber_detail'),
    url(r'^bomber/create/$', views.BomberCreate.as_view(),
        name='bomber_create'),
    url(r'^bomber/edit/(?P<pk>[0-9]+)$', views.BomberUpdate.as_view(),
        name='bomber_edit'),
    url(r'^bomber/delete/(?P<pk>[0-9]+)$', views.BomberDelete.as_view(),
        name='bomber_delete'),
    url(r'war-crime-cases/$', views.WarCrimeCaseListView.as_view(), name='browse_warcrimecases'),
    url(r'war-crime-case/detail/(?P<pk>[0-9]+)$', views.WarCrimeCaseDetailView.as_view(),
        name='warcrimecase_detail'),
    url(r'war-crime-case/create/$', views.WarCrimeCaseCreate.as_view(),
        name='warcrimecase_create'),
    url(r'war-crime-case/edit/(?P<pk>[0-9]+)$', views.WarCrimeCaseUpdate.as_view(),
        name='warcrimecase_edit'),
    url(r'war-crime-case/delete/(?P<pk>[0-9]+)$', views.WarCrimeCaseDelete.as_view(),
        name='warcrimecase_delete'),
    url(r'places-rdf/$', views.PlaceRDFView.as_view(), name='rdf_places'),
    url(r'persons-rdf/$', views.PersonRDFView.as_view(), name='rdf_persons'),
    url(r'institutions-rdf/$', views.InstitutionRDFView.as_view(), name='rdf_institutions'),
    url(r'^bombers/$', views.BomberListView.as_view(), name='browse_bombers'),
    url(r'onlineressources/$', views.OnlineRessourceListView.as_view(), name='browse_onlineressources'),
    url(r'^onlineressource/detail/(?P<pk>[0-9]+)$', views.OnlineRessourceDetailView.as_view(),
        name='onlineressource_detail'),
    url(r'^onlineressource/create/$', views.OnlineRessourceCreate.as_view(),
        name='onlineressource_create'),
    url(r'^onlineressource/edit/(?P<pk>[0-9]+)$', views.OnlineRessourceUpdate.as_view(),
        name='onlineressource_edit'),
    url(r'^onlineressource/delete/(?P<pk>[0-9]+)$', views.OnlineRessourceDelete.as_view(),
        name='onlineressource_delete'),
    url(r'personwarcrimecases/$', views.PersonWarCrimeCaseListView.as_view(), name='browse_personwarcrimecases'),
    url(r'personwarcrimecase/detail/(?P<pk>[0-9]+)$', views.PersonWarCrimeCaseDetailView.as_view(),
        name='personwarcrimecase_detail'),
    url(r'personwarcrimecase/create/$', views.PersonWarCrimeCaseCreate.as_view(),
        name='personwarcrimecase_create'),
    url(r'personwarcrimecase/edit/(?P<pk>[0-9]+)$', views.PersonWarCrimeCaseUpdate.as_view(),
        name='personwarcrimecase_edit'),
    url(r'personwarcrimecase/delete/(?P<pk>[0-9]+)$', views.PersonWarCrimeCaseDelete.as_view(),
        name='personwarcrimecase_delete'),
    url(r'airstrikes/$', views.AirstrikeListView.as_view(), name='browse_airstrikes'),
    url(r'airstrike/detail/(?P<pk>[0-9]+)$', views.AirstrikeDetailView.as_view(),
        name='airstrike_detail'),
    url(r'airstrike/create/$', views.AirstrikeCreate.as_view(),
        name='airstrike_create'),
    url(r'airstrike/edit/(?P<pk>[0-9]+)$', views.AirstrikeUpdate.as_view(),
        name='airstrike_edit'),
    url(r'airstrike/delete/(?P<pk>[0-9]+)$', views.AirstrikeDelete.as_view(),
        name='airstrike_delete'),
]
