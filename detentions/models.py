from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from idprovider.models import IdProvider, ACCURACY
from entities.models import Place, AlternativeName, Person
from vocabs.models import SkosConcept


class PrisonStation(IdProvider):

    """Holds information about prison station entities."""

    name = models.CharField(
        max_length=200, help_text="The designation of the prison station",
        verbose_name="Gefangenschaft"
        )
    alt_name = models.ManyToManyField(
        AlternativeName, max_length=200, blank=True,
        help_text="A further name for the prison station",
        verbose_name="alternative Bezeichnung des Gefangenenlagers"
        )
    station_id = models.CharField(
        max_length=50, blank=True,
        help_text="The ID for the prison station",
        verbose_name="Kennzeichen"
        )
    located_in_place = models.ForeignKey(
        Place, blank=True, null=True,
        help_text="The place where the prison camp is located",
        on_delete=models.SET_NULL, related_name='place_located',
        verbose_name="Ort der Gefangenschaft"
        )
    part_of = models.ForeignKey(
        "self", blank=True, null=True,
        help_text="The camp that this prison station is part of",
        on_delete=models.SET_NULL, verbose_name="übergeordnetes Lager"
        )
    start_date = models.DateField(
        blank=True, null=True,
        help_text="The founding date of the prison station",
        verbose_name="Gründungsdatum"
        )
    start_date_acc = models.CharField(
        max_length=50, choices=ACCURACY, default=ACCURACY[2][0],
        help_text="Accuracy of start date field",
        verbose_name="Accuracy of start date field"
        )
    end_date = models.DateField(
        blank=True, null=True,
        help_text="Date of dissolution of the prison station",
        verbose_name="Auflösungsdatum"
        )
    end_date_acc = models.CharField(
        max_length=50, choices=ACCURACY, default=ACCURACY[2][0],
        help_text="Accuracy of end date field",
        verbose_name="Accuracy of end date field"
        )
    station_type = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="Prison Station Type",
        help_text="The type of prison station",
        related_name="has_prisonstation_type",
        on_delete=models.SET_NULL
    )
    description_long = RichTextUploadingField(
        blank=True, null=True,
        verbose_name="Abstract",
        help_text="A description of the prison station",
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

    def get_delete_url(self):
        return reverse('detentions:prisonstation_delete', kwargs={'pk': self.id})

    def get_persons(self):
        ct = ContentType.objects.get(model='PersonPrison').model_class()
        items = ct.objects.filter(related_prisonstation=self)
        return items

    @classmethod
    def get_listview_url(self):
        return reverse('detentions:browse_prisonstations')

    @classmethod
    def get_class_name(self):
        class_name = self._meta.model_name
        return class_name

    @classmethod
    def get_createview_url(self):
        return reverse('detentions:prisonstation_create')

    def get_edit_url(self):
        return reverse('detentions:prisonstation_edit', kwargs={'pk': self.id})

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

    """Defines the relation between a person and the prisonstation."""

    relation_type = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        verbose_name="Type of relation",
        help_text="The type of the PersonPrison relation",
        related_name="person_prisonstation_relation",
        on_delete=models.SET_NULL
    )
    related_person = models.ForeignKey(
        Person, blank=True, null=True,
        verbose_name="Related person",
        help_text="Persons related to this PersonPrison relation",
        related_name="has_related_persons",
        on_delete=models.SET_NULL
    )
    related_prisonstation = models.ForeignKey(
        PrisonStation, blank=True, null=True,
        verbose_name="Related prison station",
        help_text="Prison stations related to this PersonPrison relation",
        related_name="related_to_prisonstation",
        on_delete=models.SET_NULL
    )
    related_location = models.ForeignKey(
        Place, blank=True, null=True,
        verbose_name="Related Location",
        help_text="Place where some interaction happend",
        related_name="related_to_personprison",
        on_delete=models.SET_NULL
    )
    start_date = models.DateField(
        blank=True, null=True,
        verbose_name="Start of relation",
        help_text="The start date of this PersonPrison relation",
    )
    start_date_acc = models.CharField(
        max_length=50, choices=ACCURACY, default=ACCURACY[2][0],
        help_text="Accuracy of start date field",
        verbose_name="Accuracy of start date field"
    )
    end_date = models.DateField(
        blank=True, null=True,
        verbose_name="End of relation",
        help_text="The end date of this PersonPrison relation",
    )
    end_date_acc = models.CharField(
        max_length=50, choices=ACCURACY, default=ACCURACY[2][0],
        help_text="Accuracy of end date field",
        verbose_name="Accuracy of end date field"
    )
    comment = models.TextField(blank=True, verbose_name="Comment", help_text="A comment")

    def __str__(self):
        if self.relation_type and self.related_person and self.related_prisonstation:
            return "{} - {}- {}".format(
                self.related_person, self.relation_type, self.related_prisonstation
            )
        elif self.relation_type and self.related_person and self.related_location:
            return "{} - {}- {}".format(
                self.related_person, self.relation_type, self.related_location
            )
        else:
            return "{}".format(self.id)

    @classmethod
    def get_listview_url(self):
        return reverse('detentions:browse_personprisons')

    @classmethod
    def get_class_name(self):
        class_name = self._meta.model_name
        return class_name

    @classmethod
    def get_createview_url(self):
        return reverse('detentions:personprison_create')

    def get_edit_url(self):
        return reverse('detentions:personprison_edit', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('detentions:personprison_delete', kwargs={'pk': self.id})

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
