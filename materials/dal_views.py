from dal import autocomplete
from entities.models import Place, Person, Bomber
from django.db.models import Q


class UsercontributionPersonAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Person.objects.all()

        if self.q:
            qs = qs.filter(written_name__icontains=self.q)

        return qs


class GedenkzeichenPersonAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Person.objects.all()

        if self.q:
            qs = qs.filter(written_name__icontains=self.q)

        return qs


class GedenkzeichenBomberAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Bomber.objects.all()

        if self.q:
            qs = qs.filter(Q(name__icontains=self.q) | Q(macr_nr__icontains=self.q))

        return qs


class GedenkzeichenPlaceAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Place.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
