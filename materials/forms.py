from django import forms
from dal import autocomplete
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, MultiField, HTML
from crispy_forms.bootstrap import Accordion, AccordionGroup

from . models import UserContribution, Gedenkzeichen


class UserContributionForm(forms.ModelForm):
    class Meta:
        model = UserContribution
        fields = "__all__"
        widgets = {
             'related_persons': autocomplete.ModelSelect2Multiple(
                url='materials-ac:usercontributionperson-autocomplete'
                )
        }

    def __init__(self, *args, **kwargs):
        super(UserContributionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class UserContributionFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(UserContributionFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'public',
                'related_persons',
                css_id="basic_search_fields"
                ),
            )


class GedenkzeichenForm(forms.ModelForm):
    class Meta:
        model = Gedenkzeichen
        fields = "__all__"
        widgets = {
            'related_person': autocomplete.ModelSelect2Multiple(
                url='materials-ac:gedenkzeichenperson-autocomplete'
            ),
            'related_bomber': autocomplete.ModelSelect2Multiple(
                url='materials-ac:gedenkzeichenbomber-autocomplete'
            ),
            'location': autocomplete.ModelSelect2(
                url='materials-ac:gedenkzeichenplace-autocomplete'
            ),
            'object_type': autocomplete.ModelSelect2(
                url='/vocabs-ac/specific-concept-ac/gedenkzeichen'
            ),
        }

    def __init__(self, *args, **kwargs):
        super(GedenkzeichenForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class GedenkzeichenFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(GedenkzeichenFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'related_person',
                css_id="basic_search_fields"
                ),
            )
