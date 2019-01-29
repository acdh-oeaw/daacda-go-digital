import django_tables2 as tables
from django_tables2.utils import A
from .models import *


class UserContributionTable(tables.Table):
    id = tables.LinkColumn(
        'materials:warcrimecase_detail',
        args=[A('pk')], verbose_name='ID'
    )
    signatur = tables.LinkColumn(
        'materials:warcrimecase_detail',
        args=[A('pk')], verbose_name='Name'
    )
    warcrimespersons = tables.TemplateColumn(
        template_name='materials/warcrimespersons.html', orderable=False,
        verbose_name='Persons mentioned in abstract'
    )
    warcrimesurls = tables.TemplateColumn(
        template_name='materials/warcrimesurls.html', orderable=False,
        verbose_name='Ressources linked to this War Crime Case'
    )

    class Meta:
        model = UserContribution
        sequence = ('id', 'signatur', 'warcrimespersons', 'warcrimesurls')
        attrs = {"class": "table table-responsive table-hover"}
