from django import forms

from .models import Board

class BoardForm(forms.Form):
    board_name = forms.CharField(label='board name', max_length=200)
