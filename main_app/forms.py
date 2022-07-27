from django.forms import ModelForm
from .models import Mood
from django import forms

class NewEntryForm(ModelForm):
  class Meta:
    model = Mood
    fields = ['date', 'headline', "description", "designation"]
    widgets = {
            'date': forms.TextInput(attrs={'class': 'form-control',
            "id": "inputDefault",
            "label": {
                "class": "col-form-label mt-4"
            }})}

           