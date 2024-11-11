from dal import autocomplete
from .models import *
from entities.models import AlternativeName, Place
from django.db.models import Q
from vocabs.models import SkosConceptScheme


class PrisonStationAltNameAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = AlternativeName.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class PrisonStationLocatedInPlaceAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Place.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class PersonPrisonLocatedInPlaceAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Place.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class PrisonStationPartOfAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = PrisonStation.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class PrisonStationStationTypeAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        try:
            selected_scheme = SkosConceptScheme.objects.get(dc_title="")
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class PersonPrisonRelationTypeAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        try:
            selected_scheme = SkosConceptScheme.objects.get(dc_title="")
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class PersonPrisonRelatedPersonsAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Person.objects.all()

        if self.q:
            qs = qs.filter(written_name__icontains=self.q)

        return qs


class PersonPrisonRelatedPrisonStationAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = PrisonStation.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
