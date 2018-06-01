import django_tables2 as tables
from django_tables2.utils import A
from entities.models import *


class WarCrimeCaseTable(tables.Table):
    id = tables.LinkColumn(
        'entities:war_crime_case_detail',
        args=[A('pk')], verbose_name='ID'
    )
    signatur = tables.LinkColumn(
        'entities:war_crime_case_detail',
        args=[A('pk')], verbose_name='Name'
    )

    class Meta:
        model = WarCrimeCase
        sequence = ('id', 'signatur',)
        attrs = {"class": "table table-responsive table-hover"}


class PersonTable(tables.Table):
    written_name = tables.LinkColumn(
        'entities:person_detail',
        args=[A('pk')], verbose_name='Written name'
    )
    rank = tables.LinkColumn(
        'entities:person_detail',
        args=[A('pk')], verbose_name='Rank'
    )
    destiny_checked = tables.LinkColumn(
        'entities:person_detail',
        args=[A('pk')], verbose_name='Destiny checked'
    )
    belongs_to_institution = tables.LinkColumn(
        'entities:person_detail',
        args=[A('pk')], verbose_name='Institution'
    )

    class Meta:
        model = Person
        sequence = ('written_name', 'rank', 'destiny_checked', 'belongs_to_institution')
        attrs = {"class": "table table-responsive table-hover"}


class BomberTable(tables.Table):
    id = tables.LinkColumn(
        'entities:bomber_detail',
        args=[A('pk')], verbose_name='ID'
    )
    name = tables.LinkColumn(
        'entities:bomber_detail',
        args=[A('pk')], verbose_name='Name'
    )
    forename = tables.Column()

    class Meta:
        model = Bomber
        sequence = ('id', 'macr_nr', 'squadron', 'date_of_crash', 'crash_place')
        attrs = {"class": "table table-responsive table-hover"}


class InstitutionTable(tables.Table):
    id = tables.LinkColumn(
        'entities:institution_detail',
        args=[A('pk')], verbose_name='ID'
    )
    written_name = tables.LinkColumn(
        'entities:institution_detail',
        args=[A('pk')], verbose_name='Name'
    )
    location = tables.Column()

    class Meta:
        model = Institution
        sequence = ('id', 'written_name',)
        attrs = {"class": "table table-responsive table-hover"}


class PlaceTable(tables.Table):
    name = tables.LinkColumn(
        'entities:place_detail',
        args=[A('pk')], verbose_name='Name'
    )
    part_of = tables.Column()

    class Meta:
        model = Place
        sequence = ('id', 'name',)
        attrs = {"class": "table table-responsive table-hover"}


class AlternativeNameTable(tables.Table):
    name = tables.LinkColumn(
        'entities:alternativename_detail',
        args=[A('pk')], verbose_name='Name'
    )

    class Meta:
        model = AlternativeName
        sequence = ('name',)
        attrs = {"class": "table table-responsive table-hover"}
