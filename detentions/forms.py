from django import forms
from .models import PrisonStation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, MultiField, HTML


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
