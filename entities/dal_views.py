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


class PersonPartOfBomberAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Bomber.objects.all()

        if self.q:
            qs = qs.filter(id__icontains=self.q)

        return qs


class PersonRankAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        try:
            selected_scheme = SkosConceptScheme.objects.get(
                dc_title='dienstgrad'
            )
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class PersonDestinyStatedAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        try:
            selected_scheme = SkosConceptScheme.objects.get(
                dc_title='eintrag'
            )
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class PersonDestinyCheckedAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        try:
            selected_scheme = SkosConceptScheme.objects.get(
                dc_title='erg'
            )
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class PersonMIAAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        try:
            selected_scheme = SkosConceptScheme.objects.get(
                dc_title=''
            )
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class OnlineRessourceRelatedPersonsAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Person.objects.all()

        if self.q:
            qs = qs.filter(written_name__icontains=self.q)

        return qs


class OnlineRessourceRelatedBombersAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Bomber.objects.all()

        if self.q:
            qs = qs.filter(macr_nr__icontains=self.q)

        return qs


class OnlineRessourceRelatedWarCrimeCasesAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = WarCrimeCase.objects.all()

        if self.q:
            qs = qs.filter(signatur__icontains=self.q)

        return qs


class PersonWarCrimeCaseRelatedPersonsAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Person.objects.all()

        if self.q:
            qs = qs.filter(written_name__icontains=self.q)

        return qs


class PersonWarCrimeCaseRelatedCasesAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = WarCrimeCase.objects.all()

        if self.q:
            qs = qs.filter(signatur__icontains=self.q)

        return qs


class PersonWarCrimeCaseRelationTypeAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        try:
            selected_scheme = SkosConceptScheme.objects.get(
                dc_title=''
            )
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class WarCrimeCaseRelatedPersonsAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Person.objects.all()

        if self.q:
            qs = qs.filter(written_name__icontains=self.q)

        return qs


class WarCrimeCaseRelatedCasesAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = WarCrimeCase.objects.all()

        if self.q:
            qs = qs.filter(signatur__icontains=self.q)

        return qs


class WarCrimeCaseRelatedPlacesAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Place.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class WarCrimeCaseCrimeTypeAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        try:
            selected_scheme = SkosConceptScheme.objects.get(
                dc_title=''
            )
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class AirstrikeTargetAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Place.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class AirstrikePlaneTypeAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        try:
            selected_scheme = SkosConceptScheme.objects.get(
                dc_title='plane_type'
            )
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class AirstrikeAirforceAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Institution.objects.all()

        if self.q:
            qs = qs.filter(written_name__icontains=self.q)

        return qs
