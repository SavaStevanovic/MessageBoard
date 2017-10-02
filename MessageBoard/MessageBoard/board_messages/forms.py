from django import forms

from .models import Board

class NameForm(forms.Form):
    Name = forms.CharField(label='Name', max_length=200)
