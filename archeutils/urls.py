from django.urls import include, path
from . import views

app_name = "archeutils"

urlpatterns = [
    path('top-col', views.top_col_md, name='top_col_md'),
    path('ids/<app_label>/<model_name>', views.get_ids, name='get_ids'),
    path(
        'md-resource/<app_label>/<model_name>/<pk>',
        views.res_as_arche_graph,
        name='res_as_arche_graph'
    ),
]
