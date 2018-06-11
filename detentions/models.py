from django.db import models
from idprovider.models import IdProvider
from entities.models import Place, AlternativeName, Person
from vocabs.models import SkosConcept
from django.urls import reverse


class PrisonStation(IdProvider):

    """Provide some Docstring"""

    name = models.CharField(
        max_length=200, help_text="Bezeichnung des Gefangenenlagers",
        verbose_name="Kriegsgefangenenlager"
        )
    alt_name = models.ManyToManyField(
        AlternativeName, max_length=200, blank=True,
        help_text="weitere Bezeichnung für das Gefangenenlager",
        verbose_name="alternative Bezeichnung des Gefangenenlagers"
        )
    station_id = models.CharField(
        max_length=50, blank=True,
        help_text="Kennzeichen für das Gefangenenlager",
        verbose_name="Kennzeichen"
        )
    located_in_place = models.ForeignKey(
        Place, blank=True, null=True,
        help_text="Ort, in dem das Gefangenenlager liegt",
        on_delete=models.SET_NULL, related_name='place_located',
        verbose_name="Ort des Lagers"
        )
    part_of = models.ForeignKey(
        "self", blank=True, null=True,
        help_text="Lager, dessen Teil dieses Gefangenenlager ist",
        on_delete=models.SET_NULL, verbose_name="übergeordnetes Lager"
        )
    start_date = models.DateField(
        blank=True, null=True,
        help_text="Gründungsdatum des Gefangenenlagers",
        verbose_name="Gründungsdatum"
        )
    end_date = models.DateField(
        blank=True, null=True,
        help_text="Auflösungsdatum des Gefangenenlagers",
        verbose_name="Auflösungsdatum"
        )
    station_type = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="Prison Station Type",
        help_text="provide some",
        related_name="has_prisonstation_type",
        on_delete=models.SET_NULL
    )

    def __str__(self):
        if self.name:
            return "{}".format(self.name)
        else:
            return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse(
            'detentions:prisonstation_detail', kwargs={'pk': self.id}
        )

    @classmethod
    def get_listview_url(self):
        return reverse('detentions:browse_prisonstations')

    @classmethod
    def get_createview_url(self):
        return reverse('detentions:prisonstation_create')

    def get_next(self):
        next = PrisonStation.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = PrisonStation.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False


class PersonPrison(IdProvider):

    """Defines the relation between a Person and the prisonstation."""

    relation_type = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="Type of the Person-PrisonStation relation",
        help_text="provide some",
        related_name="person_prisonstation_relation",
        on_delete=models.SET_NULL
    )
    related_person = models.ForeignKey(
        Person, blank=True, null=True,
        verbose_name="person",
        help_text="provide some",
        related_name="has_related_persons",
        on_delete=models.SET_NULL
    )
    related_prisonstation = models.ForeignKey(
        PrisonStation, blank=True, null=True,
        verbose_name="Prison Station",
        help_text="provide some",
        related_name="related_to_prisonstation",
        on_delete=models.SET_NULL
    )
    start_date = models.DateField(
        blank=True, null=True,
        verbose_name="start of relation",
        help_text="provide some",
    )
    end_date = models.DateField(
        blank=True, null=True,
        verbose_name="end of relation",
        help_text="provide some",
    )
    comment = models.TextField(blank=True, verbose_name="Comment")

    def __str__(self):
        if self.relation_type and self.related_person and self.related_prisonstation:
            return "{} - {}- {}".format(
                self.related_person, self.relation_type, self.related_prisonstation
            )
        else:
            return "{}".format(self.id)


    @classmethod
    def get_listview_url(self):
        return reverse('detentions:browse_personprisons')

    @classmethod
    def get_createview_url(self):
        return reverse('detentions:personprison_create')

    def get_absolute_url(self):
        return reverse(
            'detentions:personprison_detail', kwargs={'pk': self.id}
        )

    def get_next(self):
        next = PersonPrison.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = PersonPrison.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False
