import django_filters
from dal import autocomplete
from .models import UserContribution


class UserContributionListFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=UserContribution._meta.get_field('description').help_text,
        label=UserContribution._meta.get_field('description').verbose_name
    )

    class Meta:
        model = UserContribution
        fields = "__all__"
