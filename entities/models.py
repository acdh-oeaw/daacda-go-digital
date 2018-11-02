import re
import json
from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

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
    """Holds information about OnlineRessource entities."""
    www_url = models.URLField(
        blank=True, null=True,
        verbose_name="URL of online resource",
        help_text="The URL of the online resource"
    )
    description_short = models.CharField(
        max_length=250, blank=True, help_text="A short description of the online resource",
        verbose_name="Short description of online resource",
    )
    description_long = RichTextUploadingField(
        blank=True, null=True,
        verbose_name="Abstract",
        help_text="A long description of the online resource, its abstract",
    )
    related_persons = models.ManyToManyField(
        "Person",
        max_length=250, blank=True,
        verbose_name="Related persons",
        help_text="Persons related to this online resource", related_name='URLperson',
    )
    related_bombers = models.ManyToManyField(
        "Bomber",
        max_length=250, blank=True,
        verbose_name="Related bombers",
        help_text="Bombers related to this online resource", related_name='URLbomber',
    )
    related_warcrimecases = models.ManyToManyField(
        "WarCrimeCase",
        max_length=250, blank=True,
        verbose_name="Related warcrimecases",
        help_text="Warcrimecases related to this online resource", related_name='URLwarcrimecase',
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
    """Holds information about AlternativeName entities."""
    name = models.CharField(
        max_length=250, blank=True, help_text="An alternative name for a place"
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

    """Holds information about place entities."""
    name = models.CharField(
        max_length=250, blank=True, help_text="The name of the place"
    )
    alt_names = models.ManyToManyField(
        AlternativeName,
        max_length=250, blank=True,
        help_text="Alternative names for the place",
        related_name="altname_of_place"
    )
    geonames_id = models.CharField(
        max_length=50, blank=True,
        help_text="GND-ID for the place"
    )
    lat = models.DecimalField(
        max_digits=20, decimal_places=12,
        blank=True, null=True, help_text="The latitude of the place"
    )
    lng = models.DecimalField(
        max_digits=20, decimal_places=12, blank=True, null=True,
        help_text="The longitude of the place"
    )
    part_of = models.ForeignKey(
        "Place", null=True, blank=True,
        help_text="A place (country) this place is part of",
        related_name="has_child",
        on_delete=models.SET_NULL
    )
    place_type = models.CharField(
        choices=PLACE_TYPES, null=True, blank=True, max_length=50, help_text="The type of the place"
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

    def get_edit_url(self):
        return reverse('entities:place_edit', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('entities:place_delete', kwargs={'pk': self.id})

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
    """Holds information about institution entities."""
    written_name = models.CharField(
        max_length=300, blank=True,
        help_text="The name of the institution",
        verbose_name="Written name"
    )
    authority_url = models.CharField(max_length=300, blank=True)
    alt_names = models.ManyToManyField(
        AlternativeName,
        max_length=250, blank=True,
        help_text="Alternative names of the institution",
        verbose_name="Alternative Name",
        related_name="altname_of_inst"
    )
    abbreviation = models.CharField(
        max_length=300, blank=True,
        help_text="The abbreviation of the institution",)
    location = models.ForeignKey(
        Place, blank=True, null=True, on_delete=models.SET_NULL,
        help_text="The location of the institution",
    )
    parent_institution = models.ForeignKey(
        'Institution', blank=True, null=True,
        related_name='children_institutions',
        on_delete=models.SET_NULL,
        help_text="The institution the institution is part of",
    )
    comment = models.TextField(blank=True)
    related_urls = models.ManyToManyField(
        OnlineRessource,
        max_length=250, blank=True,
        verbose_name="url",
        help_text="URLs related to this institution",
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
    """Holds information about bomber entities."""
    crew_name = models.CharField(
        max_length=250, blank=True,
        verbose_name="Crewname (Pilot)",
        help_text="The name of the crew aboard this aircraft, named after the pilot",
    )
    macr_nr = models.CharField(
        max_length=50, blank=True, verbose_name="MACR-Nr",
        help_text="The Missing Air Crew Reports No."
    )
    plane_type = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="Flugzeugtyp",
        help_text="The type of the plane",
        related_name="is_plane_type",
        on_delete=models.SET_NULL
    )
    plane_id = models.CharField(
        max_length=50, blank=True, verbose_name="Flugzeugnr.",
        help_text="The plane ID",
    )
    name = models.CharField(
        max_length=250, blank=True,
        verbose_name="Flugzeugname", help_text="The name of the plane",
    )
    squadron = models.ForeignKey(
        Institution, blank=True, null=True,
        related_name="has_bomber",
        on_delete=models.SET_NULL, verbose_name="Staffel",
        help_text="The squadron the bomber belongs to",
    )
    date_of_crash = models.DateField(
        blank=True, null=True,
        verbose_name="Datum Absturz",
        help_text="The date of the bomber's crash",
    )
    reason_of_crash = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="is_crash_reason",
        on_delete=models.SET_NULL,
        verbose_name="Absturzursache",
        help_text="The reason for the bomber's crash",
    )
    target_place = models.ForeignKey(
        Place, blank=True, null=True,
        related_name="is_target_place",
        on_delete=models.SET_NULL,
        verbose_name="Zielort", help_text="The place the bomber targeted",
    )
    crash_place = models.ForeignKey(
        Place, blank=True, null=True,
        related_name="is_crashplace",
        on_delete=models.SET_NULL,
        verbose_name="Absturzort",
        help_text="The place where the bomber crashed",)
    comment = models.TextField(
        blank=True,
        verbose_name="Kommentar",
        help_text="Space for a comment")
    related_urls = models.ManyToManyField(
        OnlineRessource,
        max_length=250, blank=True,
        verbose_name="Related url",
        help_text="URLs related to this bomber",
        related_name="for_bomber"
    )
    sicht_koord = models.CharField(
        max_length=250, blank=True,
        verbose_name="Sichtung-Koord",
        help_text="Coordinates of the site the bomber was last seen at"
    )
    sicht_ort = models.CharField(
        max_length=250, blank=True,
        verbose_name="Sichtung-Ort",
        help_text="The city or village the bomber was last seen at"
    )
    sicht_land = models.CharField(
        max_length=250, blank=True,
        verbose_name="Sichtung-Land",
        help_text="The country or county the bomber was last seen at"
    )
    uhrzeit = models.CharField(
        max_length=250, blank=True,
        verbose_name="Uhrzeit",
        help_text="Time of the day"
    )
    uhrzeit_absturz = models.CharField(
        max_length=250, blank=True,
        verbose_name="Uhrzeit Absturz",
        help_text="Time of the crash"
    )
    anmerkung = models.TextField(
        blank=True,
        verbose_name="Anmerkung (Spalte Y)",
        help_text="A comment"
    )

    def __str__(self):
        return "{}".format(self.macr_nr)

    @classmethod
    def get_listview_url(self):
        return reverse('entities:browse_bombers')

    def get_edit_url(self):
        return reverse('entities:bomber_edit', kwargs={'pk': self.id})

    def get_absolute_url(self):
        return reverse('entities:bomber_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('entities:bomber_delete', kwargs={'pk': self.id})

    def get_next(self):
        next = Bomber.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Bomber.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def get_geojson(self):
        if self.target_place and self.crash_place:
            if self.target_place.lat and self.crash_place.lat:
                geojson_dict = {
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    float(self.target_place.lng),
                                    float(self.target_place.lat)
                                ]
                            },
                            "properties": {
                                "name": "{} (Place of target)".format(self.target_place.name),
                                "type": 'Place of target',
                                "self_link": self.target_place.get_absolute_url()
                            }
                        },
                        {
                            "type": "Feature",
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    float(self.crash_place.lng),
                                    float(self.crash_place.lat)
                                ]
                            },
                            "properties": {
                                "name":  "{} (Place of crash)".format(self.crash_place.name),
                                "type": 'Place of crash',
                                "self_link": self.crash_place.get_absolute_url()
                            }
                        }
                    ]
                }
            else:
                geojson_dict = None
            if geojson_dict:
                return json.dumps(geojson_dict)
            else:
                return None
        else:
            return None


class Person(IdProvider):

    """Holds information about person entities."""

    dog_tag = models.CharField(
        max_length=300, blank=True, verbose_name="Kennnummer",
        help_text="The number identifying the person"
    )
    written_name = models.CharField(
        max_length=300, blank=True, verbose_name="Name Kontrolle",
        help_text="The person's full name"
    )
    forename = models.CharField(
        max_length=300, blank=True, verbose_name="Vorname",
        help_text="The person's first name"
    )
    name = models.CharField(
        max_length=300, blank=True, verbose_name="Familienname",
        help_text="The person's second name"
    )
    middle_name = models.CharField(
        max_length=300, blank=True, verbose_name="Mittelname",
        help_text="The person's middle name"
    )
    part_of_bomber = models.ForeignKey(
        Bomber, blank=True, null=True, related_name="has_crew",
        verbose_name="Part of bomber",
        help_text="The bomber the person was part of",
        on_delete=models.SET_NULL
    )
    rank = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="is_rank",
        on_delete=models.SET_NULL, verbose_name="Dienstgrad",
        help_text="The person's rank"
    )
    destiny_stated = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="is_dest_stated",
        on_delete=models.SET_NULL, verbose_name="Eintrag MACR",
        help_text="The person's stated destiny according to MACR"
    )
    destiny_checked = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="is_dest_checked",
        on_delete=models.SET_NULL, verbose_name="Schicksal",
        help_text="The person's checked destiny"
    )
    mia = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="is_mia",
        on_delete=models.SET_NULL, verbose_name="Schicksal genau",
        help_text="The person's MIA status"
    )
    alt_names = models.ManyToManyField(
        AlternativeName,
        max_length=250, blank=True,
        verbose_name="Alternative name",
        help_text="Alternative names for the person",
        related_name="altname_of_persons"
    )
    belongs_to_institution = models.ForeignKey(
        Institution, blank=True, null=True, related_name="has_member",
        on_delete=models.SET_NULL, verbose_name="Part of institution",
        help_text="The institution the person belongs to"
    )
    place_of_birth = models.ForeignKey(
        Place, blank=True, null=True, related_name="is_birthplace",
        on_delete=models.SET_NULL, verbose_name="Geburtsort",
        help_text="The person's birthplace"
    )
    date_of_birth = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True,
        verbose_name="Geburtsdatum",
        help_text="The person's date of birth in format YYYY-MM-DD"
    )
    authority_url = models.CharField(max_length=300, blank=True)
    comment = models.TextField(
        blank=True, verbose_name="Comment", help_text="A comment"
    )
    detail = models.TextField(
        blank=True,
        verbose_name="Detail",
        help_text="Further details concerning the person"
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
        help_text="The person's nationality"
    )
    function_in_plane = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="is_crew_function",
        on_delete=models.SET_NULL, verbose_name="Funktion",
        help_text="The person's function inside the bomber"
    )

    @classmethod
    def get_createview_url(self):
        return reverse('entities:person_create')

    def get_delete_url(self):
        return reverse('entities:person_delete', kwargs={'pk': self.id})

    @classmethod
    def get_listview_url(self):
        return reverse('entities:browse_persons')

    def get_edit_url(self):
        return reverse('entities:person_edit', kwargs={'pk': self.id})

    @classmethod
    def get_arche_dump(self):
        return reverse('entities:rdf_persons')

    def get_absolute_url(self):
        return reverse('entities:person_detail', kwargs={'pk': self.id})

    def get_prisonstations(self):
        ct = ContentType.objects.get(model='PersonPrison').model_class()
        prisons = ct.objects.filter(related_person=self)
        return prisons

    def get_warcrimecases(self):
        ct = ContentType.objects.get(model='PersonWarCrimeCase').model_class()
        warcrimecases = ct.objects.filter(related_person=self)
        return warcrimecases

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

    """Holds information about war crime case entities."""

    signatur = models.CharField(
        max_length=300, blank=True,
        verbose_name="Archivsignatur",
        help_text="The formal number of the War Crime Case"
    )
    abstract = RichTextUploadingField(
        blank=True, null=True,
        verbose_name="Abstract",
        help_text="The abstract of the War Crime Case"
    )
    related_persons = models.ManyToManyField(
        Person,
        max_length=250, blank=True,
        verbose_name="Persons mentioned in abstract",
        help_text="The persons related to this War Crime Case",
        related_name="mentioned_in_abstract"
    )
    start_date = models.DateField(
        blank=True, null=True,
        verbose_name="Start date",
        help_text="The day the War Crime Case started"
    )
    end_date = models.DateField(
        blank=True, null=True,
        verbose_name="End date",
        help_text="The day the War Crime Case ended"
    )
    date_accuracy_start = models.CharField(
        default="Y", max_length=3, choices=DATE_ACCURACY,
        blank=True, null=True,
        verbose_name="Date accuracy start date",
        help_text="An information stating whether the given start date is accurate"
    )
    date_accuracy_end = models.CharField(
        default="Y", max_length=3, choices=DATE_ACCURACY,
        blank=True, null=True,
        verbose_name="Date accuracy end date",
        help_text="An information stating whether the given end date is accurate"
    )
    related_urls = models.ManyToManyField(
        OnlineRessource,
        max_length=250, blank=True,
        verbose_name="Related URLs",
        help_text="URLs related to this War Crime Case",
        related_name="for_warcrimecase"
    )
    related_cases = models.ManyToManyField(
        'self',
        max_length=250, blank=True,
        verbose_name="Related cases",
        help_text="Other cases related to this War Crime Case",
        related_name="has_related_cases"
    )
    related_places = models.ManyToManyField(
        Place,
        max_length=250, blank=True,
        verbose_name="Places mentioned in abstract",
        help_text="Places related to this War Crime Case",
        related_name="wcc_mentiones_places"
    )
    type_of_crime = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="crime_type_of",
        on_delete=models.SET_NULL, verbose_name="Type of crime",
        help_text="The type of crime committed in this War Crime Case"
    )
    tried = models.CharField(
        blank=True, null=True,
        max_length=250,
        choices=TRIED,
        help_text="An information stating whether this War Crime Case was tried or not"
    )

    @classmethod
    def get_createview_url(self):
        return reverse('entities:warcrimecase_create')

    @classmethod
    def get_listview_url(self):
        return reverse('entities:browse_warcrimecases')

    def get_edit_url(self):
        return reverse('entities:warcrimecase_edit', kwargs={'pk': self.id})

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

    def get_persons(self):
        ct = ContentType.objects.get(model='PersonWarCrimeCase').model_class()
        items = ct.objects.filter(related_case=self)
        return items

    def __str__(self):
        if self.signatur:
            return "{}".format(self.signatur)
        else:
            return "{}".format(self.id)


class PersonWarCrimeCase(IdProvider):
    """Holds information about war crime case entities associated with a specific person."""
    start_date = models.DateField(
        blank=True, null=True,
        verbose_name="Start date",
        help_text="The start date of this PersonWarCrimeCase relation"
    )
    end_date = models.DateField(
        blank=True, null=True,
        verbose_name="End date",
        help_text="The end date of this PersonWarCrimeCase relation"
    )
    comment = models.TextField(
        blank=True, verbose_name="Comment", help_text="A comment"
    )
    related_case = models.ForeignKey(
        WarCrimeCase,
        max_length=250, blank=True, null=True,
        verbose_name="Related case",
        help_text="Case related to this PersonWarCrimeCase relation",
        related_name="related_to_person",
        on_delete=models.SET_NULL
    )
    related_person = models.ForeignKey(
        Person,
        max_length=250, blank=True,
        verbose_name="Persons mentioned in abstract",
        help_text="Person related to this PersonWarCrimeCase relation",
        related_name="has_related_warcase", null=True,
        on_delete=models.SET_NULL
    )
    relation_type = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="relation_type_of",
        on_delete=models.SET_NULL, verbose_name="Type of relation",
        help_text="The type of this PersonWarCrimeCase relation"
    )
    relation_by_crime = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name="relation_by_crime",
        on_delete=models.SET_NULL, verbose_name="Art Verbrechen",
        help_text="The type of this PersonWarCrimeCase relation"
    )

    @classmethod
    def get_createview_url(self):
            return reverse('entities:personwarcrimecase_create')

    @classmethod
    def get_listview_url(self):
            return reverse('entities:browse_personwarcrimecases')

    def get_edit_url(self):
        return reverse('entities:personwarcrimecase_edit', kwargs={'pk': self.id})

    def get_absolute_url(self):
            return reverse('entities:personwarcrimecase_detail', kwargs={'pk': self.id})

    def get_next(self):
        next = PersonWarCrimeCase.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = PersonWarCrimeCase.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def __str__(self):
        return "{}".format(self.id)


class Airstrike(IdProvider):
    """Holds information about air raids targeting Austrian territory."""
    date = models.DateField(
        blank=True, null=True,
        verbose_name="Date",
        help_text="The day the airstrike took place"
    )
    target = models.ForeignKey(
        Place,
        max_length=250, blank=True, null=True,
        verbose_name="Target place of the airstrike",
        help_text="Place targeted by the airstrike", on_delete=models.SET_NULL,
        related_name="is_target",
    )
    plane_type = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="Plane type",
        help_text="The type of the plane",
        related_name="is_plane_type_2",
        on_delete=models.SET_NULL,
    )
    number_of_planes = models.IntegerField(
        blank=True, null=True, verbose_name="Total", help_text="Estimated number of planes involved in total"
    )
    airforce = models.ForeignKey(
        Institution, max_length=250, blank=True, null=True,
        verbose_name="Airforce",
        help_text="Name of the Airforce involved in the attack", on_delete=models.SET_NULL,
        related_name="run_airstrike",
    )

    @classmethod
    def get_createview_url(self):
        return reverse('entities:airstrike_create')

    @classmethod
    def get_listview_url(self):
        return reverse('entities:browse_airstrikes')

    def get_absolute_url(self):
        return reverse('entities:airstrike_detail', kwargs={'pk': self.id})

    def get_next(self):
        next = Airstrike.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Airstrike.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def __str__(self):
        return "{}".format(self.date)
