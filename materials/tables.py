import django_tables2 as tables
from django_tables2.utils import A
from .models import *


class UserContributionTable(tables.Table):
    id = tables.LinkColumn()

    class Meta:
        model = UserContribution
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}


class GedenkzeichenTable(tables.Table):
    id = tables.LinkColumn()

    class Meta:
        model = Gedenkzeichen
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}
