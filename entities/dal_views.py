from dal import autocomplete
from .models import *
from django.db.models import Q
from vocabs.models import SkosConceptScheme


class AlternativeNameAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = AlternativeName.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class PlaceAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Place.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class PersonAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Person.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class InstitutionAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Institution.objects.all()

        if self.q:
            qs = qs.filter(written_name__icontains=self.q)

        return qs


class BomberPlaneTypeAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        # try:
        selected_scheme = SkosConceptScheme.objects.get(
            dc_title='plane_type'
            )
        qs = SkosConcept.objects.filter(scheme=selected_scheme)
        # except:
        #     qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class BomberSquadronAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Institution.objects.all()

        if self.q:
            qs = qs.filter(written_name__icontains=self.q)

        return qs


class BomberReasonOfCrashAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        try:
            selected_scheme = SkosConceptScheme.objects.get(
                dc_title='reason_of_crash'
            )
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs
