from django.contrib import admin
from .models import Place, AlternativeName, Bomber, Institution, Person, WarCrimeCase, OnlineRessource, Airstrike
from detentions.models import PrisonStation, PersonPrison


class BomberAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'date_of_crash',
        'macr_nr',
        'plane_type',
        'target_place',
        'crash_place',
        'reason_of_crash',
    )
    list_filter = [
        'plane_type',
        'reason_of_crash',
    ]
    search_fields = [
        'name',
    ]


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'written_name',
        'part_of_bomber',
        'dog_tag',
    )
    list_filter = [
        'destiny_stated',
    ]

    search_fields = [
        'written_name',
    ]


admin.site.register(WarCrimeCase)
admin.site.register(Place)
admin.site.register(Institution)
admin.site.register(AlternativeName)
admin.site.register(Bomber, BomberAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(OnlineRessource)
admin.site.register(PrisonStation)
admin.site.register(PersonPrison)
admin.site.register(Airstrike)
