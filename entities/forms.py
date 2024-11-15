from django import forms
from dal import autocomplete
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.bootstrap import Accordion, AccordionGroup
from .models import (
    Place,
    AlternativeName,
    Institution,
    Person,
    Bomber,
    WarCrimeCase,
    OnlineRessource,
    PersonWarCrimeCase,
    Airstrike,
)


class PersonFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PersonFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.helper.form_tag = False
        self.add_input(Submit("Filter", "Search"))
        self.layout = Layout(
            Fieldset(
                "Basic search options",
                "name",
                "written_name",
                css_id="basic_search_fields",
            ),
            Accordion(
                AccordionGroup(
                    "Advanced search", "part_of_bomber", "place_of_birth", css_id="more"
                ),
            ),
        )


class OnlineRessourceFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(OnlineRessourceFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.helper.form_tag = True
        self.add_input(Submit("Filter", "Search"))
        self.layout = Layout(
            Fieldset(
                "Basic search options", "related_persons", css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup("Advanced search", "www_url", css_id="more"),
            ),
        )


class WarCrimeCaseForm(forms.ModelForm):
    class Meta:
        model = WarCrimeCase
        fields = "__all__"
        widgets = {
            "abstract": CKEditorUploadingWidget(),
            "related_persons": autocomplete.ModelSelect2Multiple(
                url="entities-ac:warcrimecaserelatedpersons-autocomplete"
            ),
            "related_cases": autocomplete.ModelSelect2Multiple(
                url="entities-ac:warcrimecaserelatedcases-autocomplete"
            ),
            "related_places": autocomplete.ModelSelect2Multiple(
                url="entities-ac:warcrimecaserelatedplaces-autocomplete"
            ),
            "type_of_crime": autocomplete.ModelSelect2(
                url="entities-ac:warcrimecasecrimetype-autocomplete"
            ),
        }

    def __init__(self, *args, **kwargs):
        super(WarCrimeCaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class OnlineRessourceForm(forms.ModelForm):
    class Meta:
        model = OnlineRessource
        fields = "__all__"
        widgets = {
            "abstract": CKEditorUploadingWidget(),
            "related_persons": autocomplete.ModelSelect2Multiple(
                url="entities-ac:onlineressourcerelatedpersons-autocomplete"
            ),
            "related_bombers": autocomplete.ModelSelect2(
                url="entities-ac:onlineressourcerelatedbombers-autocomplete"
            ),
            "related_warcrimecases": autocomplete.ModelSelect2Multiple(
                url="entities-ac:onlineressourcerelatedwarcrimecases-autocomplete"
            ),
        }

    def __init__(self, *args, **kwargs):
        super(OnlineRessourceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        widgets = {
            "belongs_to_institution": autocomplete.ModelSelect2(
                url="entities-ac:institution-autocomplete"
            ),
            "place_of_birth": autocomplete.ModelSelect2(
                url="entities-ac:place-autocomplete"
            ),
            "alt_names": autocomplete.ModelSelect2Multiple(
                url="entities-ac:altname-autocomplete"
            ),
            "part_of_bomber": autocomplete.ModelSelect2(
                url="entities-ac:personpartofbomber-autocomplete"
            ),
            "rank": autocomplete.ModelSelect2(
                url="entities-ac:personrank-autocomplete"
            ),
            "destiny_stated": autocomplete.ModelSelect2(
                url="entities-ac:persondestinystated-autocomplete"
            ),
            "destiny_checked": autocomplete.ModelSelect2(
                url="entities-ac:persondestinychecked-autocomplete"
            ),
            "mia": autocomplete.ModelSelect2(url="entities-ac:personmia-autocomplete"),
            "nation": autocomplete.ModelSelect2(
                url="/vocabs-ac/specific-concept-ac/nationality"
            ),
        }

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class BomberFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(BomberFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.helper.form_tag = False
        self.add_input(Submit("Filter", "Search"))
        self.layout = Layout(
            Fieldset(
                "Basic search options", "name", "macr_nr", css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup(
                    "Advanced search",
                    "target_place",
                    "crash_place",
                    "squadron",
                    "reason_of_crash",
                    css_id="more",
                ),
            ),
        )


class BomberForm(forms.ModelForm):
    class Meta:
        model = Bomber
        fields = "__all__"
        widgets = {
            "plane_type": autocomplete.ModelSelect2(
                url="entities-ac:bomberplanetype-autocomplete"
            ),
            "squadron": autocomplete.ModelSelect2(
                url="entities-ac:bombersquadron-autocomplete"
            ),
            "reason_of_crash": autocomplete.ModelSelect2(
                url="entities-ac:bomberreasonofcrash-autocomplete"
            ),
            "target_place": autocomplete.ModelSelect2(
                url="entities-ac:place-autocomplete"
            ),
            "last_seen": autocomplete.ModelSelect2(
                url="entities-ac:place-autocomplete"
            ),
            "crash_place": autocomplete.ModelSelect2(
                url="entities-ac:place-autocomplete"
            ),
        }

    def __init__(self, *args, **kwargs):
        super(BomberForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class WarCrimeCaseFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(WarCrimeCaseFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.helper.form_tag = False
        self.add_input(Submit("Filter", "Search"))
        self.layout = Layout(
            Fieldset(
                "Basic search options",
                "signatur",
                "related_persons",
                css_id="basic_search_fields",
            ),
            Accordion(
                AccordionGroup(
                    "Advanced search", "start_date", "abstract", css_id="more"
                ),
            ),
        )


class InstitutionFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(InstitutionFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.helper.form_tag = False
        self.add_input(Submit("Filter", "Search"))
        self.layout = Layout(
            Fieldset(
                "Basic search options",
                "written_name",
                "alt_names",
                css_id="basic_search_fields",
            ),
            Accordion(
                AccordionGroup("Advanced search", "authority_url", css_id="more"),
            ),
        )


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = "__all__"
        widgets = {
            "location": autocomplete.ModelSelect2(url="entities-ac:place-autocomplete"),
            "parent_institution": autocomplete.ModelSelect2(
                url="entities-ac:institution-autocomplete"
            ),
            "alt_names": autocomplete.ModelSelect2Multiple(
                url="entities-ac:altname-autocomplete"
            ),
        }

    def __init__(self, *args, **kwargs):
        super(InstitutionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class AlternativeNameForm(forms.ModelForm):
    class Meta:
        model = AlternativeName
        fields = "__all__"
        widgets = {
            "name": autocomplete.ModelSelect2(url="entities-ac:altname-autocomplete"),
        }

    def __init__(self, *args, **kwargs):
        super(AlternativeNameForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class AlternativeNameFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(AlternativeNameFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.helper.form_tag = False
        self.add_input(Submit("Filter", "Search"))
        self.layout = Layout(
            Fieldset("Basic search options", "name", css_id="basic_search_fields"),
        )


class AlternativeNameFormCreate(forms.ModelForm):
    class Meta:
        model = AlternativeName
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(AlternativeNameFormCreate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class PlaceFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PlaceFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.helper.form_tag = False
        self.add_input(Submit("Filter", "Search"))
        self.layout = Layout(
            Fieldset(
                "Basic search options",
                "name",
                "alt_names",
                css_id="basic_search_fields",
            ),
            Accordion(
                AccordionGroup(
                    "Advanced search", "geonames_id", "part_of", css_id="more"
                ),
            ),
        )


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = "__all__"
        widgets = {
            "part_of": autocomplete.ModelSelect2(url="entities-ac:place-autocomplete"),
            "alt_names": autocomplete.ModelSelect2Multiple(
                url="entities-ac:altname-autocomplete"
            ),
        }

    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class PlaceFormCreate(forms.ModelForm):
    class Meta:
        model = Place
        fields = "__all__"
        widgets = {
            "part_of": autocomplete.ModelSelect2(url="entities-ac:place-autocomplete"),
            "alt_names": autocomplete.ModelSelect2Multiple(
                url="entities-ac:altname-autocomplete"
            ),
        }

    def __init__(self, *args, **kwargs):
        super(PlaceFormCreate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class PersonWarCrimeCaseForm(forms.ModelForm):
    class Meta:
        model = PersonWarCrimeCase
        fields = "__all__"
        widgets = {
            "related_persons": autocomplete.ModelSelect2(
                url="entities-ac:personwarcrimecaserelatedpersons-autocomplete"
            ),
            "related_cases": autocomplete.ModelSelect2(
                url="entities-ac:personwarcrimecaserelatedcases-autocomplete"
            ),
            "relation_type": autocomplete.ModelSelect2(
                url="entities-ac:personwarcrimecaserelationtype-autocomplete"
            ),
        }

    def __init__(self, *args, **kwargs):
        super(PersonWarCrimeCaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class PersonWarCrimeCaseFilterFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(PersonWarCrimeCaseFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.helper.form_tag = False
        self.add_input(Submit("Filter", "Search"))
        self.layout = Layout(
            Fieldset(
                "Basic search options", "related_person", css_id="basic_search_fields"
            ),
        )


class AirstrikeForm(forms.ModelForm):
    class Meta:
        model = Airstrike
        fields = "__all__"
        widgets = {
            "target": autocomplete.ModelSelect2(
                url="entities-ac:airstriketarget-autocomplete"
            ),
            "plane_type": autocomplete.ModelSelect2(
                url="entities-ac:airstrikeplanetype-autocomplete"
            ),
            "airforce": autocomplete.ModelSelect2(
                url="entities-ac:airstrikeairforce-autocomplete"
            ),
        }

    def __init__(self, *args, **kwargs):
        super(AirstrikeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class AirstrikeFormCreate(forms.ModelForm):
    class Meta:
        model = Airstrike
        fields = "__all__"
        widgets = {
            "target": autocomplete.ModelSelect2(
                url="entities-ac:airstriketarget-autocomplete"
            ),
            "plane_type": autocomplete.ModelSelect2(
                url="entities-ac:airstrikeplanetype-autocomplete"
            ),
            "airforce": autocomplete.ModelSelect2(
                url="entities-ac:airstrikeairforce-autocomplete"
            ),
        }

    def __init__(self, *args, **kwargs):
        super(AirstrikeFormCreate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class AirstrikeFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(AirstrikeFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.helper.form_tag = False
        self.add_input(Submit("Filter", "Search"))
        self.layout = Layout(
            Fieldset(
                "Basic search options", "date", "target", css_id="basic_search_fields"
            ),
        )
