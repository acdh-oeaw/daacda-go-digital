import django_filters
from dal import autocomplete
from entities.models import (
    Place,
    AlternativeName,
    Institution,
    Person,
    Bomber,
    WarCrimeCase,
    OnlineRessource,
    PersonWarCrimeCase,
    Airstrike,
)
from vocabs.models import SkosConcept


django_filters.filters.LOOKUP_TYPES = [
    ("", "---------"),
    ("exact", "Is equal to"),
    ("iexact", "Is equal to (case insensitive)"),
    ("not_exact", "Is not equal to"),
    ("lt", "Lesser than/before"),
    ("gt", "Greater than/after"),
    ("gte", "Greater than or equal to"),
    ("lte", "Lesser than or equal to"),
    ("startswith", "Starts with"),
    ("endswith", "Ends with"),
    ("contains", "Contains"),
    ("icontains", "Contains (case insensitive)"),
    ("not_contains", "Does not contain"),
]


class WarCrimeCaseListFilter(django_filters.FilterSet):
    signatur = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=WarCrimeCase._meta.get_field("signatur").help_text,
        label=WarCrimeCase._meta.get_field("signatur").verbose_name,
    )
    related_persons = django_filters.ModelMultipleChoiceFilter(
        queryset=Person.objects.all(),
        help_text=WarCrimeCase._meta.get_field("related_persons").help_text,
        label=WarCrimeCase._meta.get_field("related_persons").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/entities-ac/specific-person-ac/mentioned_in_abstract",
        ),
    )

    class Meta:
        model = WarCrimeCase
        fields = "__all__"


class PersonListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Person._meta.get_field("name").help_text,
        label=Person._meta.get_field("name").verbose_name,
    )
    forename = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Person._meta.get_field("forename").help_text,
        label=Person._meta.get_field("forename").verbose_name,
    )
    written_name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text="Search in the Person's full name",
        label="Firstname, Middlename, Lastname",
    )
    place_of_birth = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Person._meta.get_field("place_of_birth").help_text,
        label=Person._meta.get_field("place_of_birth").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/entities-ac/specific-place-ac/is_birthplace",
        ),
    )
    belongs_to_institution = django_filters.ModelMultipleChoiceFilter(
        queryset=Institution.objects.all(),
        help_text=Person._meta.get_field("belongs_to_institution").help_text,
        label=Person._meta.get_field("belongs_to_institution").verbose_name,
    )

    class Meta:
        model = Person
        fields = "__all__"


class BomberListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Bomber._meta.get_field("name").help_text,
        label=Bomber._meta.get_field("name").verbose_name,
    )
    target_place = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Bomber._meta.get_field("target_place").help_text,
        label=Bomber._meta.get_field("target_place").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/entities-ac/specific-place-ac/is_target_place",
        ),
    )
    crash_place = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Bomber._meta.get_field("crash_place").help_text,
        label=Bomber._meta.get_field("crash_place").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/entities-ac/specific-place-ac/is_crashplace",
        ),
    )
    reason_of_crash = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.all(),
        help_text=Bomber._meta.get_field("reason_of_crash").help_text,
        label=Bomber._meta.get_field("reason_of_crash").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/reason_of_crash",
            attrs={
                "data-placeholder": "Start typing to get suggestions ...",
                "data-minimum-input-length": 1,
            },
        ),
    )

    class Meta:
        model = Bomber
        fields = "__all__"


class InstitutionListFilter(django_filters.FilterSet):
    written_name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Institution._meta.get_field("written_name").help_text,
        label=Institution._meta.get_field("written_name").verbose_name,
    )
    alt_names = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Institution._meta.get_field("alt_names").help_text,
        label=Institution._meta.get_field("alt_names").verbose_name,
    )
    authority_url = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Institution._meta.get_field("authority_url").help_text,
        label=Institution._meta.get_field("authority_url").verbose_name,
    )

    class Meta:
        model = Institution
        fields = ["id", "written_name", "authority_url"]


class PlaceListFilter(django_filters.FilterSet):
    name = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Place._meta.get_field("name").help_text,
        label=Place._meta.get_field("name").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="entities-ac:place-autocomplete",
        ),
    )
    geonames_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Place._meta.get_field("geonames_id").help_text,
        label=Place._meta.get_field("geonames_id").verbose_name,
    )
    alt_names = django_filters.ModelMultipleChoiceFilter(
        queryset=AlternativeName.objects.all(),
        help_text=Place._meta.get_field("alt_names").help_text,
        label=Place._meta.get_field("alt_names").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="entities-ac:altname-autocomplete",
        ),
    )
    part_of = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Place._meta.get_field("part_of").help_text,
        label=Place._meta.get_field("part_of").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="entities-ac:search-region-autocomplete",
        ),
    )

    class Meta:
        model = Place
        fields = ["id", "name"]


class CrashPlaceListFilter(django_filters.FilterSet):
    name = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Place._meta.get_field("name").help_text,
        label=Place._meta.get_field("name").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/entities-ac/specific-place-ac/is_crashplace",
        ),
    )
    geonames_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Place._meta.get_field("geonames_id").help_text,
        label=Place._meta.get_field("geonames_id").verbose_name,
    )
    alt_names = django_filters.ModelMultipleChoiceFilter(
        queryset=AlternativeName.objects.all(),
        help_text=Place._meta.get_field("alt_names").help_text,
        label=Place._meta.get_field("alt_names").verbose_name,
    )
    part_of = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Place._meta.get_field("part_of").help_text,
        label=Place._meta.get_field("part_of").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/entities-ac/specific-place-ac/part_of",
        ),
    )

    class Meta:
        model = Place
        fields = ["id", "name", "geonames_id", "alt_names", "part_of"]


class AlternativeNameListFilter(django_filters.FilterSet):
    name = django_filters.ModelMultipleChoiceFilter(
        queryset=AlternativeName.objects.all(),
        help_text=AlternativeName._meta.get_field("name").help_text,
        label=AlternativeName._meta.get_field("name").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="entities-ac:altname-autocomplete",
        ),
    )

    class Meta:
        model = AlternativeName
        fields = ["id", "name"]


class OnlineRessourceListFilter(django_filters.FilterSet):
    www_url = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=OnlineRessource._meta.get_field("www_url").help_text,
        label=OnlineRessource._meta.get_field("www_url").verbose_name,
    )
    related_persons = django_filters.ModelMultipleChoiceFilter(
        queryset=Person.objects.all(),
        help_text=OnlineRessource._meta.get_field("related_persons").help_text,
        label=OnlineRessource._meta.get_field("related_persons").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="entities-ac:person-autocomplete",
        ),
    )

    class Meta:
        model = OnlineRessource
        fields = ["www_url", "related_persons"]


class PersonWarCrimeCaseListFilter(django_filters.FilterSet):
    related_person = django_filters.ModelMultipleChoiceFilter(
        queryset=Person.objects.all(),
        help_text=PersonWarCrimeCase._meta.get_field("related_person").help_text,
        label=PersonWarCrimeCase._meta.get_field("related_person").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="entities-ac:person-autocomplete",
        ),
    )

    class Meta:
        model = PersonWarCrimeCase
        fields = "__all__"


class AirstrikeListFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Airstrike._meta.get_field("date").help_text,
        label=Airstrike._meta.get_field("date").verbose_name,
    )
    target = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Airstrike._meta.get_field("target").help_text,
        label=Airstrike._meta.get_field("target").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/entities-ac/specific-place-ac/is_target",
        ),
    )

    class Meta:
        model = Airstrike
        fields = [
            "date",
            "target",
            "plane_type",
            "airforce",
        ]
