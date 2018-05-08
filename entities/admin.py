from django.contrib import admin
from .models import Place, AlternativeName, Bomber, Institution


class BomberAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'macr_nr',
        'plane_type',
        'target_place',
        'last_seen',
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


admin.site.register(Place)
admin.site.register(Institution)
admin.site.register(AlternativeName)
admin.site.register(Bomber, BomberAdmin)
