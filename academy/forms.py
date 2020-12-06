from django.forms import ModelForm
from django import forms
from .models import Etudiant

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)

class EtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        fields ='__all__'
