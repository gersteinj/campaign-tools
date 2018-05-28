from django import forms
from django.forms import ModelForm
from .models import Roster

class CreateRosterForm(ModelForm):
    class Meta:
        model = Roster
        exclude = ['owner']