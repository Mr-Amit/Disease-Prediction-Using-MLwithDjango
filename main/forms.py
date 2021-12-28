from django import forms
from django.forms import fields
from .store import getsymptoms

symptoms = getsymptoms()


# FRUIT_CHOICES= [
#     ('orange', 'Oranges'),
#     ('cantaloupe', 'Cantaloupes'),
#     ('mango', 'Mangoes'),
#     ('honeydew', 'Honeydews'),
#     ]
symptoms.sort()
ss = [tuple([x,x.replace('_', ' ').title()]) for x in symptoms]

class SymptomForm(forms.Form):
    
    symptom1 = forms.CharField(label='Symptom 1',
        widget=forms.Select(choices=ss))
    symptom2 = forms.CharField(label='Symptom 2',
        widget=forms.Select(choices=ss))
    symptom3 = forms.CharField(label='Symptom 3',
        widget=forms.Select(choices=ss))
    symptom4 = forms.CharField(label='Symptom 4',
        widget=forms.Select(choices=ss))
    symptom5 = forms.CharField(label='Symptom 5',
        widget=forms.Select(choices=ss))

    class Meta:
        fields = ['symptom1','symptom2','symptom3','symptom4','symptom5']