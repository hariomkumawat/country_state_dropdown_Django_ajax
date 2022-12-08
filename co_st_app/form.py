from django import forms

from django import forms

from .models import *


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

