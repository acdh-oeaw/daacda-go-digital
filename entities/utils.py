from django.conf import settings
from . models import Institution, Place

bomb_group = Institution.objects.filter(inst_type__pref_label=settings.BOMB_GROUP_LABEL).distinct()
airforce = Institution.objects.filter(inst_type__pref_label=settings.AIR_FORCE_LABEL).distinct()
squad = Institution.objects.filter(inst_type__pref_label=settings.SQUAD_LABEL).distinct()
crash_places = Place.objects.filter(is_crashplace__isnull=False).distinct()
attack_places = Place.objects.filter(is_target__isnull=False).distinct()
