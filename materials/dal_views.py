from dal import autocomplete
from .models import *
from entities.models import AlternativeName, Place
from django.db.models import Q
from vocabs.models import SkosConceptScheme


class UsercontributionPersonAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Person.objects.all()

        if self.q:
            qs = qs.filter(written_name__icontains=self.q)

        return qs
