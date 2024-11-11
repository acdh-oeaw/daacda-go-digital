import django_tables2 as tables
from django_tables2.utils import A
from entities.models import *


class WarCrimeCaseTable(tables.Table):
    id = tables.LinkColumn(
        "entities:warcrimecase_detail", args=[A("pk")], verbose_name="ID"
    )
    signatur = tables.LinkColumn(
        "entities:warcrimecase_detail", args=[A("pk")], verbose_name="Name"
    )
    warcrimespersons = tables.TemplateColumn(
        template_name="entities/warcrimespersons.html",
        orderable=False,
        verbose_name="Persons mentioned in abstract",
    )
    warcrimesurls = tables.TemplateColumn(
        template_name="entities/warcrimesurls.html",
        orderable=False,
        verbose_name="Ressources linked to this War Crime Case",
    )

    class Meta:
        model = WarCrimeCase
        sequence = ("id", "signatur", "warcrimespersons", "warcrimesurls")
        attrs = {"class": "table table-responsive table-hover"}


class OnlineRessourceTable(tables.Table):
    www_url = tables.LinkColumn(
        "entities:onlineressource_detail", args=[A("pk")], verbose_name="URL"
    )
    onlineressourcepersons = tables.TemplateColumn(
        template_name="entities/onlineressourcepersons.html",
        orderable=False,
        verbose_name="Persons linked to this ressource",
    )
    onlineressourcebombers = tables.TemplateColumn(
        template_name="entities/onlineressourcebombers.html",
        orderable=False,
        verbose_name="Bombers linked to this ressource",
    )
    onlineressourcewarcrimecases = tables.TemplateColumn(
        template_name="entities/onlineressourcewarcrimecases.html",
        orderable=False,
        verbose_name="War crime cases linked to this ressource",
    )

    class Meta:
        model = OnlineRessource
        sequence = (
            "www_url",
            "onlineressourcepersons",
            "onlineressourcebombers",
            "onlineressourcewarcrimecases",
        )
        attrs = {"class": "table table-responsive table-hover"}


class PersonTable(tables.Table):
    written_name = tables.LinkColumn(
        "entities:person_detail", args=[A("pk")], verbose_name="Written name"
    )
    rank = tables.LinkColumn(
        "entities:person_detail", args=[A("pk")], verbose_name="Rank"
    )
    destiny_checked = tables.LinkColumn(
        "entities:person_detail", args=[A("pk")], verbose_name="Destiny checked"
    )
    belongs_to_institution = tables.LinkColumn(
        "entities:person_detail", args=[A("pk")], verbose_name="Institution"
    )

    class Meta:
        model = Person
        sequence = ("written_name", "rank", "destiny_checked", "belongs_to_institution")
        attrs = {"class": "table table-responsive table-hover"}


class BomberTable(tables.Table):
    id = tables.LinkColumn("entities:bomber_detail", args=[A("pk")], verbose_name="ID")
    name = tables.LinkColumn(
        "entities:bomber_detail", args=[A("pk")], verbose_name="Name"
    )
    forename = tables.Column()

    class Meta:
        model = Bomber
        sequence = (
            "id",
            "macr_nr",
            "squadron",
            "date_of_crash",
            "crash_place",
        )
        attrs = {"class": "table table-responsive table-hover"}


class InstitutionTable(tables.Table):
    id = tables.LinkColumn(
        "entities:institution_detail", args=[A("pk")], verbose_name="ID"
    )
    written_name = tables.LinkColumn(
        "entities:institution_detail", args=[A("pk")], verbose_name="Name"
    )
    location = tables.Column()

    class Meta:
        model = Institution
        sequence = (
            "id",
            "written_name",
        )
        attrs = {"class": "table table-responsive table-hover"}


class PlaceTable(tables.Table):
    name = tables.LinkColumn(
        "entities:place_detail", args=[A("pk")], verbose_name="Name"
    )
    part_of = tables.Column()

    class Meta:
        model = Place
        sequence = (
            "id",
            "name",
        )
        attrs = {"class": "table table-responsive table-hover"}


class AlternativeNameTable(tables.Table):
    name = tables.LinkColumn(
        "entities:alternativename_detail", args=[A("pk")], verbose_name="Name"
    )

    class Meta:
        model = AlternativeName
        sequence = ("name",)
        attrs = {"class": "table table-responsive table-hover"}


class PersonWarCrimeCaseTable(tables.Table):
    id = tables.LinkColumn("entities:personwarcrimecase_detail", args=[A("pk")])

    class Meta:
        model = PersonWarCrimeCase
        sequence = (
            "id",
            "related_person",
            "relation_type",
            "related_case",
        )
        attrs = {"class": "table table-responsive table-hover"}


class AirstrikeTable(tables.Table):
    date = tables.LinkColumn("entities:airstrike_detail", args=[A("pk")])

    class Meta:
        model = Airstrike
        sequence = ("date",)
        attrs = {"class": "table table-responsive table-hover"}
