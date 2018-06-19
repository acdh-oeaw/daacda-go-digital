from django import forms
from dal import autocomplete
from .models import PrisonStation, PersonPrison
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, MultiField, HTML
from crispy_forms.bootstrap import Accordion, AccordionGroup


class PrisonStationForm(forms.ModelForm):
    class Meta:
        model = PrisonStation
        fields = "__all__"
        widgets = {
            'alt_name': autocomplete.ModelSelect2(
                url='detentions-ac:prisonstationaltname-autocomplete'),
            'located_in_place': autocomplete.ModelSelect2(
                url='detentions-ac:prisonstationlocatedinplace-autocomplete'),
            'part_of': autocomplete.ModelSelect2(
                url='detentions-ac:prisonstationpartof-autocomplete'),
            'station_type': autocomplete.ModelSelect2(
                url='detentions-ac:prisonstationstationtype-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(PrisonStationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class PrisonStationFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PrisonStationFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'name',
                'written_name',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'acad_title',
                    'alt_names',
                    'authority_url',
                    'belongs_to_institution',
                    css_id="more"
                    ),
                )
            )


class PersonPrisonForm(forms.ModelForm):
    class Meta:
        model = PersonPrison
        fields = "__all__"
        widgets = {
            'relation_type': autocomplete.ModelSelect2(
                url='detentions-ac:personprisonrelationtype-autocomplete'),
            'related_person': autocomplete.ModelSelect2(
                url='detentions-ac:personprisonrelatedpersons-autocomplete'),
            'related_prisonstation': autocomplete.ModelSelect2(
                url='detentions-ac:personprisonrelatedprisonstation-autocomplete'),
            }

    def __init__(self, *args, **kwargs):
        super(PersonPrisonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class PersonPrisonFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PersonPrisonFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'name',
                'written_name',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'acad_title',
                    'alt_names',
                    'authority_url',
                    'belongs_to_institution',
                    css_id="more"
                    ),
                )
            )
