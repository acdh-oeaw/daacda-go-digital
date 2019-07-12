import django_filters
from dal import autocomplete
from .models import UserContribution
from entities.models import (
    Person
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
