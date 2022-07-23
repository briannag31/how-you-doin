from django.forms import ModelForm
from .models import Mood
from django import forms
# MOODS = (
#     ('G', 'Good Day'),
#     ('O', 'OK Day'),
#     ('B', 'Bad Day')
# )

# class NewEntryForm(forms.Form):
#     date = forms.DateField(label='Date')
#     headline = forms.CharField(max_length=100)
#     description = forms.TextInput(max_length=500)
#     designation = forms.CharField(
#     max_length=1,
#     choices=MOODS,
#     default=MOODS[0][0]
#   )
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

           