import re
import json
from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from entities.models import Bomber, Person, WarCrimeCase
from vocabs.models import SkosConcept


BOOLEAN_CHOICES = (
    (True, "Yes"),
    (False, "No")
)


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
