from django import forms
from django.forms import ModelForm,ModelMultipleChoiceField
from Service.models import Service,ServiceType,Parameter_Concept

class ServiceNameForm(forms.Form):
    service_name = forms.CharField(label='Service Name')
class ServiceForm(ModelForm):
    input_concepts = ModelMultipleChoiceField(
        queryset=Parameter_Concept.objects.filter(is_input=True),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    output_concepts = ModelMultipleChoiceField(
        queryset=Parameter_Concept.objects.filter(is_input=False),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Service
        fields=['name','cost','type','input_concepts','output_concepts']