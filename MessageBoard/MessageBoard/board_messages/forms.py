from django import forms

from .models import Board,Card

class NameForm(forms.Form):
    Name = forms.CharField(label='Title', max_length=200)
    
class UpdateForm(forms.ModelForm):
        class Meta:
            model = Card
            fields = ['card_text',]
