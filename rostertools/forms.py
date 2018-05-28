from django import forms
from django.forms import ModelForm
from .models import Roster, Unit

class RosterForm(ModelForm):
    class Meta:
        model = Roster
        exclude = ['owner']

class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'