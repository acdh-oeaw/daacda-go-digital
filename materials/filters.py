import django_filters
from dal import autocomplete
from .models import UserContribution, Gedenkzeichen
from entities.models import (
    Person, Bomber, Place
)

class UserContributionListFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=UserContribution._meta.get_field('description').help_text,
        label=UserContribution._meta.get_field('description').verbose_name
    )
    related_persons = django_filters.ModelMultipleChoiceFilter(
        queryset=Person.objects.all(),
        help_text=UserContribution._meta.get_field('related_persons').help_text,
        label=UserContribution._meta.get_field('related_persons').verbose_name,
        widget=autocomplete.Select2Multiple(
            url='materials-ac:usercontributionperson-autocomplete',
        )
    )

    class Meta:
        model = UserContribution
        fields = "__all__"


class GedenkzeichenListFilter(django_filters.FilterSet):
    related_person = django_filters.ModelMultipleChoiceFilter(
        queryset=Person.objects.all(),
        help_text=Gedenkzeichen._meta.get_field('related_person').help_text,
        label=Gedenkzeichen._meta.get_field('related_person').verbose_name,
        widget=autocomplete.Select2Multiple(
            url='materials-ac:gedenkzeichenperson-autocomplete',
        )
    )
    related_bomber = django_filters.ModelMultipleChoiceFilter(
        queryset=Bomber.objects.all(),
        help_text=Gedenkzeichen._meta.get_field('related_bomber').help_text,
        label=Gedenkzeichen._meta.get_field('related_bomber').verbose_name,
        widget=autocomplete.Select2Multiple(
            url='materials-ac:gedenkzeichenbomber-autocomplete',
        )
    )
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Gedenkzeichen._meta.get_field('location').help_text,
        label=Gedenkzeichen._meta.get_field('location').verbose_name,
        widget=autocomplete.Select2Multiple(
            url='materials-ac:gedenkzeichenplace-autocomplete',
        )
    )

    class Meta:
        model = Gedenkzeichen
        fields = "__all__"
