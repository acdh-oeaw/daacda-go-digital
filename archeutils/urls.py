from django.urls import include, path
from . import views

app_name = "archeutils"

urlpatterns = [
    path('md/top-col', views.top_col_md, name='top_col_md'),
    path('<app_label>/<model_name>/<pk>', views.res_as_arche_graph, name='res_as_arche_graph'),
    # path('<app_label>/<model_name>', views.qs_as_arche_graph, name='qs_as_arche_graph'),
]
