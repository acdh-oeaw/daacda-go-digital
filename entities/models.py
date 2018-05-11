import re
from django.db import models
from django.urls import reverse
from idprovider.models import IdProvider
from vocabs.models import SkosConcept


class AlternativeName(IdProvider):
    name = models.CharField(
        max_length=250, blank=True, help_text="Alternative Name"
    )

    def get_absolute_url(self):
        return reverse(
            'entities:alternativename_detail', kwargs={'pk': self.id}
        )

    @classmethod
    def get_listview_url(self):
        return reverse('entities:browse_altnames')

    @classmethod
    def get_createview_url(self):
        return reverse('entities:alternativename_create')

    def get_next(self):
        next = AlternativeName.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = AlternativeName.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def get_absolute_url(self):
        return reverse(
            'entities:alternativename_detail', kwargs={'pk': self.id}
        )

    def __str__(self):
        return "{}".format(self.name)


class Place(IdProvider):
    PLACE_TYPES = (
        ("city", "city"),
        ("country", "country"),
        ("region", "region"),
    )

    """Holds information about entities."""
    name = models.CharField(
        max_length=250, blank=True, help_text="Normalized name"
    )
    alt_names = models.ManyToManyField(
        AlternativeName,
        max_length=250, blank=True,
        help_text="Alternative names",
        related_name="altname_of_place"
    )
    geonames_id = models.CharField(
        max_length=50, blank=True,
        help_text="GND-ID"
    )
    lat = models.DecimalField(
        max_digits=20, decimal_places=12,
        blank=True, null=True
    )
    lng = models.DecimalField(
        max_digits=20, decimal_places=12, blank=True, null=True
    )
    part_of = models.ForeignKey(
        "Place", null=True, blank=True,
        help_text="A place (country) this place is part of.",
        related_name="has_child",
        on_delete=models.SET_NULL
    )
    place_type = models.CharField(
        choices=PLACE_TYPES, null=True, blank=True, max_length=50
    )

    def get_geonames_url(self):
        if self.geonames_id.startswith('ht') and self.geonames_id.endswith('.html'):
            return self.geonames_id
        elif self.geonames_id.startswith('ht'):
            return self.geonames_id
        else:
            return "http://www.geonames.org/{}".format(self.geonames_id)

    def get_geonames_rdf(self):
        try:
            number = re.findall(r'\d+', str(self.geonames_id))[0]
            return None
        except:
            return None

    def save(self, *args, **kwargs):
        if self.geonames_id:
            new_id = self.get_geonames_url()
            self.geonames_id = new_id
        super(Place, self).save(*args, **kwargs)

    @classmethod
    def get_listview_url(self):
        return reverse('entities:browse_places')

    @classmethod
    def get_createview_url(self):
        return reverse('entities:place_create')

    @classmethod
    def get_arche_dump(self):
        return reverse('entities:rdf_places')

    def get_next(self):
        next = Place.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Place.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def get_absolute_url(self):
        return reverse('entities:place_detail', kwargs={'pk': self.id})

    def __str__(self):
        return "{}".format(self.name)


class Institution(IdProvider):
    written_name = models.CharField(max_length=300, blank=True)
    authority_url = models.CharField(max_length=300, blank=True)
    alt_names = models.ManyToManyField(
        AlternativeName,
        max_length=250, blank=True,
        help_text="Alternative names",
        related_name="altname_of_inst"
    )
    abbreviation = models.CharField(max_length=300, blank=True)
    location = models.ForeignKey(
        Place, blank=True, null=True, on_delete=models.SET_NULL
    )
    parent_institution = models.ForeignKey(
        'Institution', blank=True, null=True, related_name='children_institutions',
        on_delete=models.SET_NULL
    )
    comment = models.TextField(blank=True)

    @classmethod
    def get_arche_dump(self):
        return reverse('entities:rdf_institutions')

    @classmethod
    def get_listview_url(self):
        return reverse('entities:browse_institutions')

    @classmethod
    def get_createview_url(self):
        return reverse('entities:institution_create')

    def get_absolute_url(self):
        return reverse('entities:institution_detail', kwargs={'pk': self.id})

    def get_next(self):
        next = Institution.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Institution.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def __str__(self):
        return "{}".format(self.written_name)


class Bomber(models.Model):
    import_name = models.CharField(
        max_length=250, blank=True, verbose_name="Bombername", help_text="import_name some"
    )
    macr_nr = models.CharField(
        max_length=50, blank=True, verbose_name="MARC-Nr", help_text="provide some"
    )
    plane_type = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="plane_type",
        help_text="provide some",
        related_name="is_plane_type",
        on_delete=models.SET_NULL
    )
    plane_id = models.CharField(max_length=50, blank=True, verbose_name="The aircraft´s ID")
    name = models.CharField(max_length=250, blank=True, verbose_name="Name of the aircraft")
    squadron = models.ForeignKey(
        Institution, blank=True, null=True,
        related_name="has_bomber",
        on_delete=models.SET_NULL
    )
    date_of_crash = models.DateField(blank=True, null=True)
    reason_of_crash = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="is_crash_reason",
        on_delete=models.SET_NULL
    )
    target_place = models.ForeignKey(
        Place, blank=True, null=True,
        related_name="is_target_place",
        on_delete=models.SET_NULL
    )
    last_seen = models.ForeignKey(
        Place, blank=True, null=True,
        related_name="is_last_seen",
        on_delete=models.SET_NULL)
    crash_place = models.ForeignKey(
        Place, blank=True, null=True,
        related_name="is_crashplace",
        on_delete=models.SET_NULL)
    lat = models.DecimalField(max_digits=20, decimal_places=12, blank=True, null=True)
    lng = models.DecimalField(max_digits=20, decimal_places=12, blank=True, null=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return "{}".format(self.macr_nr)


class Person(IdProvider):

    """provide some docstring"""

    dog_tag = models.CharField(
        max_length=300, blank=True, verbose_name="dog_tag", help_text="provide some"
    )
    written_name = models.CharField(max_length=300, blank=True)
    forename = models.CharField(max_length=300, blank=True)
    name = models.CharField(max_length=300, blank=True)
    part_of_bomber = models.ForeignKey(
        Bomber, blank=True, null=True, related_name="has_crew",
        on_delete=models.SET_NULL
    )
    rank = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="rank",
        help_text="provide some",
        related_name="is_rank",
        on_delete=models.SET_NULL
    )
    destiny_stated = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="destiny_stated",
        help_text="provide some",
        related_name="is_dest_stated",
        on_delete=models.SET_NULL
    )
    destiny_checked = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="destiny_checked",
        help_text="provide some",
        related_name="is_dest_checked",
        on_delete=models.SET_NULL
    )
    mia = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="mia",
        help_text="provide some",
        related_name="is_mia",
        on_delete=models.SET_NULL
    )
    position = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="position",
        help_text="provide some",
        related_name="is_position",
        on_delete=models.SET_NULL
    )
    alt_names = models.ManyToManyField(
        AlternativeName,
        max_length=250, blank=True,
        help_text="Alternative names",
        related_name="altname_of_persons"
    )
    belongs_to_institution = models.ForeignKey(
        Institution, blank=True, null=True, related_name="has_member",
        on_delete=models.SET_NULL
    )
    place_of_birth = models.ForeignKey(
        Place, blank=True, null=True, related_name="is_birthplace",
        on_delete=models.SET_NULL
    )
    date_of_birth = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True,
        verbose_name="Date of Birth",
        help_text="YYYY-MM-DD"
    )
    authority_url = models.CharField(max_length=300, blank=True)
    comment = models.TextField(blank=True)
    # = models.TextField(blank=True)

    @classmethod
    def get_createview_url(self):
        return reverse('entities:person_create')

    @classmethod
    def get_listview_url(self):
        return reverse('entities:browse_persons')

    @classmethod
    def get_arche_dump(self):
        return reverse('entities:rdf_persons')

    def get_absolute_url(self):
        return reverse('entities:person_detail', kwargs={'pk': self.id})

    def get_next(self):
        next = Person.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Person.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def __str__(self):
        if self.written_name:
            return "{}".format(self.written_name)
        elif self.name and self.forename:
            return "{}, {}".format(self.name, self.forename)
        else:
            return "No name provided"
