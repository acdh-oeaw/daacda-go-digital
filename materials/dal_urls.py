from django.conf.urls import url
from . import views
from . import dal_views
from .models import *

app_name = 'vocabs'

urlpatterns = [
    url(
        r'^usercontributionperson-autocomplete/$',
        dal_views.UsercontributionPersonAC.as_view(model=Person, create_field='written_name',),
        name='usercontributionperson-autocomplete',
    ),
]
