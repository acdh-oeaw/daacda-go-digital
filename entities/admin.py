from django.contrib import admin
from .models import Place, AlternativeName, Bomber, Institution

admin.site.register(Place)
admin.site.register(Institution)
admin.site.register(AlternativeName)
admin.site.register(Bomber)
