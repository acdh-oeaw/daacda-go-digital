import re
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from idprovider.models import IdProvider
from vocabs.models import SkosConcept

DATE_ACCURACY = (
    ('Y', 'Year'),
    ('YM', 'Month'),
    ('DMY', 'Day')
)


class OnlineRessource(IdProvider):

    www_url = models.URLField(
        blank=True, null=True,
        verbose_name="URL of online ressource",
        help_text="provide some"
    )
    description_short = models.CharField(
        max_length=250, blank=True, help_text="short_description",
        verbose_name="Short description of online ressource",
    )
    description_long = RichTextUploadingField(
        blank=True, null=True,
        verbose_name="Abstract",
        help_text="Provide some",
    )
    related_persons = models.ManyToManyField(
        "Person",
        max_length=250, blank=True,
        verbose_name="Related persons",
        help_text="provide Some", related_name='URLperson',
    )
    related_bombers = models.ManyToManyField(
        "Bomber",
        max_length=250, blank=True,
        verbose_name="Related bombers",
        help_text="provide Some", related_name='URLbomber',
    )
    related_warcrimecases = models.ManyToManyField(
        "WarCrimeCase",
        max_length=250, blank=True,
        verbose_name="Related warcrimecases",
        help_text="provide Some", related_name='URLwarcrimecase',
    )

    def __str__(self):
        if self.www_url:
            return "{}".format(self.www_url)
        else:
            return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse(
            'entities:onlineressource_detail', kwargs={'pk': self.id}
        )

    @classmethod
    def get_listview_url(self):
        return reverse('entities:browse_onlineressources')

    @classmethod
    def get_createview_url(self):
        return reverse('entities:onlineressource_create')

    def get_next(self):
        next = OnlineRessource.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = OnlineRessource.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False


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
        'Institution', blank=True, null=True,
        related_name='children_institutions', on_delete=models.SET_NULL
    )
    comment = models.TextField(blank=True)
    related_urls = models.ManyToManyField(
        OnlineRessource,
        max_length=250, blank=True,
        verbose_name="url",
        help_text="provide Some",
        related_name="for_institution"
    )

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
        max_length=250, blank=True, verbose_name="Flugzeugname",
        help_text="provide some"
    )
    crew_name = models.CharField(
        max_length=250, blank=True,
        verbose_name="Crewname (Pilot)",
        help_text="provide some"
    )
    macr_nr = models.CharField(
        max_length=50, blank=True, verbose_name="MACR-No.",
        help_text="provide some"
    )
    plane_type = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="Plane Type",
        help_text="provide some",
        related_name="is_plane_type",
        on_delete=models.SET_NULL
    )
    plane_id = models.CharField(
        max_length=50, blank=True, verbose_name="Flugzeug Nr."
    )
    name = models.CharField(
        max_length=250, blank=True, verbose_name="Flugzeug Name")
    squadron = models.ForeignKey(
        Institution, blank=True, null=True,
        related_name="has_bomber",
        on_delete=models.SET_NULL, verbose_name="Squadron"
    )
    date_of_crash = models.DateField(
        blank=True, null=True, verbose_name="Date of Crash"
    )
    reason_of_crash = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="is_crash_reason",
        on_delete=models.SET_NULL, verbose_name="Reason for Crash"
    )
    target_place = models.ForeignKey(
        Place, blank=True, null=True,
        related_name="is_target_place",
        on_delete=models.SET_NULL, verbose_name="Target Place"
    )
    last_seen = models.ForeignKey(
        Place, blank=True, null=True,
        related_name="is_last_seen",
        on_delete=models.SET_NULL, verbose_name="Last seen in")
    crash_place = models.ForeignKey(
        Place, blank=True, null=True,
        related_name="is_crashplace",
        on_delete=models.SET_NULL, verbose_name="Crash Place")
    lat = models.DecimalField(
        max_digits=20, decimal_places=12, blank=True, null=True,
        verbose_name="Latitude"
    )
    lng = models.DecimalField(
        max_digits=20, decimal_places=12, blank=True, null=True,
        verbose_name="Longitude"
    )
    comment = models.TextField(blank=True, verbose_name="Comment")
    related_urls = models.ManyToManyField(
        OnlineRessource,
        max_length=250, blank=True,
        verbose_name="url",
        help_text="provide Some",
        related_name="for_bomber"
    )
    sicht_koord = models.CharField(
        max_length=250, blank=True,
        verbose_name="Sichtung-Koord",
        help_text="provide some"
    )
    sicht_ort = models.CharField(
        max_length=250, blank=True,
        verbose_name="Sichtung-Ort",
        help_text="provide some"
    )
    sicht_land = models.CharField(
        max_length=250, blank=True,
        verbose_name="Sichtung-Land",
        help_text="provide some"
    )
    uhrzeit = models.CharField(
        max_length=250, blank=True,
        verbose_name="Uhrzeit",
        help_text="provide some"
    )
    uhrzeit_absturz = models.CharField(
        max_length=250, blank=True,
        verbose_name="Uhrzeit Absturz",
        help_text="provide some"
    )
    anmerkung = models.TextField(
        blank=True,
        verbose_name="Anmerkung (Spalte Y)",
        help_text="provide some"
    )

    def __str__(self):
        return "{}".format(self.macr_nr)

    @classmethod
    def get_listview_url(self):
        return reverse('entities:browse_bombers')


class Person(IdProvider):

    """provide some docstring"""

    dog_tag = models.CharField(
        max_length=300, blank=True, verbose_name="Kennnummer",
        help_text="provide some"
    )
    written_name = models.CharField(
        max_length=300, blank=True, verbose_name="Written name",
        help_text="provide some"
    )
    forename = models.CharField(
        max_length=300, blank=True, verbose_name="First name",
        help_text="Person's first name"
    )
    name = models.CharField(
        max_length=300, blank=True, verbose_name="Surname",
        help_text="Person's second name"
    )
    middle_name = models.CharField(
        max_length=300, blank=True, verbose_name="Mittelname",
        help_text="Person's middle name"
    )
    part_of_bomber = models.ForeignKey(
        Bomber, blank=True, null=True, related_name="has_crew",
        verbose_name="Part of bomber",
        help_text="Bomber the person was part of",
        on_delete=models.SET_NULL
    )
    rank = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="is_rank",
        on_delete=models.SET_NULL, verbose_name="Rank",
        help_text="Person's rank"
    )
    destiny_stated = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="is_dest_stated",
        on_delete=models.SET_NULL, verbose_name="Eintrag MACR",
        help_text="Person's stated destiny"
    )
    destiny_checked = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="is_dest_checked",
        on_delete=models.SET_NULL, verbose_name="Schicksal",
        help_text="Person's checked destiny"
    )
    mia = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="is_mia",
        on_delete=models.SET_NULL, verbose_name="Schicksal genau",
        help_text="Person's MIA status"
    )
    position = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="Position",
        help_text="provide some",
        related_name="is_position",
        on_delete=models.SET_NULL
    )
    alt_names = models.ManyToManyField(
        AlternativeName,
        max_length=250, blank=True,
        verbose_name="Alternative name",
        help_text="Person's alternative name",
        related_name="altname_of_persons"
    )
    belongs_to_institution = models.ForeignKey(
        Institution, blank=True, null=True, related_name="has_member",
        on_delete=models.SET_NULL, verbose_name="Part of institution",
        help_text="Institution person belongs to"
    )
    place_of_birth = models.ForeignKey(
        Place, blank=True, null=True, related_name="is_birthplace",
        on_delete=models.SET_NULL, verbose_name="Place of birth",
        help_text="Person's birthplace"
    )
    date_of_birth = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True,
        verbose_name="Date of birth",
        help_text="Person's date of birth in format YYYY-MM-DD"
    )
    authority_url = models.CharField(max_length=300, blank=True)
    comment = models.TextField(
        blank=True, verbose_name="Comment", help_text="Comment"
    )
    detail = models.TextField(
        blank=True, verbose_name="Detail", help_text="provide some"
    )
    related_urls = models.ManyToManyField(
        OnlineRessource,
        max_length=250, blank=True,
        verbose_name="Related URLs",
        help_text="URLs related to this person",
        related_name="for_person"
    )
    nation = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="is_nationality",
        on_delete=models.SET_NULL, verbose_name="Nationalität",
        help_text="provide some"
    )
    function_in_plane = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="is_crew_function",
        on_delete=models.SET_NULL, verbose_name="Funktion",
        help_text="provide some"
    )
    # ToDo: detail

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


TRIED = (
    ('tried', 'tried'),
    ('not tried', 'not tried')
)


class WarCrimeCase(IdProvider):

    """provide some docstring"""

    signatur = models.CharField(
        max_length=300, blank=True,
        verbose_name="Archivsignatur",
        help_text="Provide Some"
    )
    abstract = RichTextUploadingField(
        blank=True, null=True,
        verbose_name="Abstract",
        help_text="Provide some"
    )
    related_persons = models.ManyToManyField(
        Person,
        max_length=250, blank=True,
        verbose_name="Persons mentioned in abstract",
        help_text="erwähnte Personen",
        related_name="mentioned_in_abstract"
    )
    start_date = models.DateField(
        blank=True, null=True,
        verbose_name="Start date",
        help_text="Provide Some"
    )
    end_date = models.DateField(
        blank=True, null=True,
        verbose_name="End date",
        help_text="Provide Some"
    )
    date_accuracy = models.CharField(
        default="Y", max_length=3, choices=DATE_ACCURACY,
        blank=True, null=True, verbose_name="Date accuracy",
    )
    related_urls = models.ManyToManyField(
        OnlineRessource,
        max_length=250, blank=True,
        verbose_name="Related URLs",
        help_text="provide Some",
        related_name="for_warcrimecase"
    )
    related_cases = models.ManyToManyField(
        'self',
        max_length=250, blank=True,
        verbose_name="Related cases",
        help_text="Erwähnte Fälle",
        related_name="has_related_cases"
    )
    related_places = models.ManyToManyField(
        Place,
        max_length=250, blank=True,
        verbose_name="Places mentioned in abstract",
        help_text="Erwähnte Orte",
        related_name="wcc_mentiones_places"
    )
    type_of_crime = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="crime_type_of",
        on_delete=models.SET_NULL, verbose_name="Type of crime",
        help_text="provide some"
    )
    tried = models.CharField(
        blank=True, null=True,
        max_length=250, choices=TRIED
    )

    @classmethod
    def get_createview_url(self):
        return reverse('entities:warcrimecase_create')

    @classmethod
    def get_listview_url(self):
        return reverse('entities:browse_warcrimecases')

    def get_absolute_url(self):
        return reverse('entities:warcrimecase_detail', kwargs={'pk': self.id})

    def get_next(self):
        next = WarCrimeCase.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = WarCrimeCase.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def __str__(self):
        if self.signatur:
            return "{}".format(self.signatur)
        else:
            return "{}".format(self.id)


class PersonWarCrimeCase(IdProvider):

    start_date = models.DateField(
        blank=True, null=True,
        verbose_name="Start date",
        help_text="Provide Some"
    )
    end_date = models.DateField(
        blank=True, null=True,
        verbose_name="End date",
        help_text="Provide Some"
    )
    comment = models.TextField(blank=True, verbose_name="Comment")
    related_cases = models.ForeignKey(
        WarCrimeCase,
        max_length=250, blank=True, null=True,
        verbose_name="Related cases",
        help_text="erwähnte Personen",
        related_name="has_related_cases_2",
        on_delete=models.SET_NULL
    )
    related_persons = models.ForeignKey(
        Person,
        max_length=250, blank=True,
        verbose_name="Persons mentioned in abstract",
        help_text="erwähnte Personen",
        related_name="has_related_persons_2", null=True,
        on_delete=models.SET_NULL
    )
    relation_type = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="relation_type_of",
        on_delete=models.SET_NULL, verbose_name="Type of relation",
        help_text="provide some"
    )
