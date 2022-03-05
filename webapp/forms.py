from django import forms
from .excuse_choices import categories

class ExcusesForm(forms.Form):
    category = forms.ChoiceField(choices=categories)
    number = forms.IntegerField()