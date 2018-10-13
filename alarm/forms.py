from django import forms
from django.forms import ModelForm
from django.urls import reverse

from .models import player
from django.utils import timezone
GROUP = (
    ('두산','두산'),
    ('롯데','롯데'),
)
PLAYER = (
    ('추신수','추신수'),
    ('류현진','류현진'),
)

class playerForm(forms.ModelForm):

    class Meta:
        model = player
        fields = ('group','player')
        labels = {
            'group': '응원팀',
            'player': '응원선수',
        }
        widgets = {
            'group': forms.CheckboxSelectMultiple(choices = GROUP),
            'player': forms.CheckboxSelectMultiple(choices = PLAYER),

        }