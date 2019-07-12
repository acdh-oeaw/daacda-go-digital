from django.conf.urls import url
from . import views

app_name = 'materials'

urlpatterns = [
    url(r'^usercontributions/$', views.UserContributionListView.as_view(),
        name='browse_usercontributions'),
    url(r'^usercontribution/detail/(?P<pk>[0-9]+)$', views.UserContributionDetailView.as_view(),
        name='usercontribution_detail'),
    url(r'^usercontribution/create/$', views.UserContributionCreate.as_view(),
        name='usercontribution_create'),
    url(r'^usercontribution/edit/(?P<pk>[0-9]+)$', views.UserContributionUpdate.as_view(),
        name='usercontribution_edit'),
    url(r'^usercontribution/delete/(?P<pk>[0-9]+)$', views.UserContributionDelete.as_view(),
        name='usercontribution_delete'),
    url(r'^gedenkzeichen/$', views.GedenkzeichenListView.as_view(),
        name='browse_gedenkzeichen'),
    url(r'^gedenkzeichen/detail/(?P<pk>[0-9]+)$', views.GedenkzeichenDetailView.as_view(),
        name='gedenkzeichen_detail'),
    url(r'^gedenkzeichen/create/$', views.GedenkzeichenCreate.as_view(),
        name='gedenkzeichen_create'),
    url(r'^gedenkzeichen/edit/(?P<pk>[0-9]+)$', views.GedenkzeichenUpdate.as_view(),
        name='gedenkzeichen_edit'),
    url(r'^gedenkzeichen/delete/(?P<pk>[0-9]+)$', views.GedenkzeichenDelete.as_view(),
        name='gedenkzeichen_delete'),
]
