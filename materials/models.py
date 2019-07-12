import re
import json
from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from entities.models import Bomber, Person, Place, WarCrimeCase, DATE_ACCURACY
from vocabs.models import SkosConcept


BOOLEAN_CHOICES = (
    (True, "Yes"),
    (False, "No")
)


class Gedenkzeichen(models.Model):
    """ provide some information """

    name = models.CharField(
        max_length=250, blank=True,
        help_text="Name des Gedenkzeichens"
    )
    start_date = models.DateField(
        blank=True, null=True,
        verbose_name="Start date",
        help_text="The day the Gedenkzeichen started"
    )
    end_date = models.DateField(
        blank=True, null=True,
        verbose_name="End date",
        help_text="The day the Gedenkzeichen ended"
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
    object_type = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        related_name='is_gedenkzeichentyp_of',
        on_delete=models.SET_NULL,
        verbose_name="The Gedenkzeichens type",
        help_text="The Gedenkzeichens type",
    )
    location = models.ForeignKey(
        Place, blank=True, null=True, on_delete=models.SET_NULL,
        help_text="The location of the Gedenkzeichen",
        related_name='location_of_gedenkzeichen',
    )
    related_person = models.ForeignKey(
        Person, blank=True, null=True,
        verbose_name="Related person",
        help_text="Persons related to this Gedenkzeichen relation",
        related_name="gd_has_related_persons",
        on_delete=models.SET_NULL
    )
    related_bomber = models.ForeignKey(
        Bomber, blank=True, null=True,
        verbose_name="Related bomber",
        help_text="Persons related to this Gedenkzeichen relation",
        related_name="gd_has_related_bombers",
        on_delete=models.SET_NULL
    )
    description = RichTextUploadingField(
        blank=True, null=True,
        verbose_name="Description",
        help_text="Description",
    )
    legacy_id = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.id)


class UserContribution(models.Model):
    """ Exposes material sent in by database users """
    description = RichTextUploadingField(
        blank=True, null=True,
        verbose_name="Description",
        help_text="Description",
    )
    donater_name = models.CharField(
        max_length=250, blank=True,
        help_text="Name of the person who provided the material"
    )
    public = models.BooleanField(
        default=False, verbose_name="Public",
        choices=BOOLEAN_CHOICES,
        help_text="Should this entry (and all related entries) be public"
    )
    content_checked_by = models.ForeignKey(
        User, blank=True, null=True, related_name="content_checked_by_user",
        verbose_name="Checked by",
        help_text="Who checked the entered data.",
        on_delete=models.SET_NULL
    )
    related_persons = models.ManyToManyField(
        Person,
        max_length=250, blank=True,
        verbose_name="Related persons",
        help_text="Persons related to this online resource", related_name='usercontribution_person',
    )
    related_bombers = models.ManyToManyField(
        Bomber,
        max_length=250, blank=True,
        verbose_name="Related bombers",
        help_text="Bombers related to this online resource", related_name='usercontribution_bomber',
    )
    related_warcrimecases = models.ManyToManyField(
        WarCrimeCase,
        max_length=250, blank=True,
        verbose_name="Related warcrimecases",
        help_text="Warcrimecases related to this online resource",
        related_name='usercontribution_warcrimecase',
    )
    legacy_id = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse(
            'materials:usercontribution_detail', kwargs={'pk': self.id}
        )

    @classmethod
    def get_class_name(self):
        class_name = self._meta.model_name
        return class_name

    @classmethod
    def get_listview_url(self):
        return reverse('materials:browse_usercontributions')

    def get_edit_url(self):
        return reverse('materials:usercontribution_edit', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('materials:usercontribution_delete', kwargs={'pk': self.id})

    @classmethod
    def get_createview_url(self):
        return reverse('materials:usercontribution_create')

    def get_next(self):
        next = UserContribution.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = UserContribution.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False
