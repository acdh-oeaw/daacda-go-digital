import django_tables2 as tables
from django_tables2.utils import A
from detentions.models import *


class PrisonStationTable(tables.Table):
    name = tables.LinkColumn(
        'detentions:prisonstation_detail',
        args=[A('pk')], verbose_name='Kriegsgefangenenlager'
    )

    class Meta:
        model = PrisonStation
        sequence = (
            'name', 'station_id', 'located_in_place',
        )
        attrs = {"class": "table table-responsive table-hover"}


class PersonPrisonTable(tables.Table):

    class Meta:
        model = PersonPrison
        sequence = (
            'relation_type', 'related_person', 'related_prisonstation',
        )
        attrs = {"class": "table table-responsive table-hover"}
