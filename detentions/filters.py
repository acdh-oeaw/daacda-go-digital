import django_filters
from dal import autocomplete
from detentions.models import PrisonStation, PersonPrison
from entities.models import (
    Place, AlternativeName, Institution, Person, Bomber, WarCrimeCase,
    OnlineRessource, PersonWarCrimeCase, Airstrike
)

django_filters.filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('iexact', 'Is equal to (case insensitive)'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than/before'),
    ('gt', 'Greater than/after'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('icontains', 'Contains (case insensitive)'),
    ('not_contains', 'Does not contain'),
]


class PrisonStationListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=PrisonStation._meta.get_field('name').help_text,
        label=PrisonStation._meta.get_field('name').verbose_name
        )

    class Meta:
        model = PrisonStation
        fields = "__all__"


class PersonPrisonListFilter(django_filters.FilterSet):
    relation_type = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=PersonPrison._meta.get_field('relation_type').help_text,
        label=PersonPrison._meta.get_field('relation_type').verbose_name
        )
    related_person = django_filters.ModelMultipleChoiceFilter(
        queryset=Person.objects.all(),
        help_text=PersonPrison._meta.get_field('related_person').help_text,
        label=PersonPrison._meta.get_field('related_person').verbose_name,
        widget=autocomplete.Select2Multiple(
            url='entities-ac:person-autocomplete',
            )
    )

    class Meta:
        model = PersonPrison
        fields = "__all__"
