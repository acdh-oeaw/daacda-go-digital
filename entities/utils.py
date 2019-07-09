from django.conf import settings
from . models import Institution

bomb_group = Institution.objects.filter(inst_type__pref_label=settings.BOMB_GROUP_LABEL)
