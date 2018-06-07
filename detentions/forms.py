from django import forms
from .models import PrisonStation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, MultiField, HTML
from crispy_forms.bootstrap import Accordion, AccordionGroup


class PrisonStationForm(forms.ModelForm):
    class Meta:
        model = PrisonStation
        fields = "__all__"

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
