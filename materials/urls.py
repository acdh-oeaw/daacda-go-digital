from django.conf.urls import url
from . import views

app_name = 'materials'

urlpatterns = [
    url(
        r'^usercontributions/$', views.UserContributionListView.as_view(),
        name='browse_usercontributions'
    ),
    url(r'^usercontribution/detail/(?P<pk>[0-9]+)$', views.UserContributionDetailView.as_view(),
        name='usercontribution_detail'),
    url(r'^usercontribution/create/$', views.UserContributionCreate.as_view(),
        name='usercontribution_create'),
    url(r'^usercontribution/edit/(?P<pk>[0-9]+)$', views.UserContributionUpdate.as_view(),
        name='usercontribution_edit'),
    url(r'^usercontribution/delete/(?P<pk>[0-9]+)$', views.UserContributionDelete.as_view(),
        name='usercontribution_delete'),
]
