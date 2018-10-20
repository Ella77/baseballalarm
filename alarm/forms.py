from django import forms
from django.forms import ModelForm
from django.urls import reverse

from .models import player
from django.utils import timezone
SITUATION = (
                ('주자없음','주자없음'),
                ('1루','1루'),
                ('2루','2루'),
                ('1, 2루','1, 2루'),
                ('3루', '3루'),
                ('1, 3루', '1 ,3루'),
                ('2, 3루','2, 3루'),
                ('만루', '만루'),

)
TEAM = (
    ('한화', '한화'),
    ('넥센', '넥선'),
)


class playerForm(forms.ModelForm):

    class Meta:
        model = player
        fields = ('team','situation','player')
        labels = {

            'team':'응원팀',
            'player': '응원선수',
            'situation': '관심상황',
        }
        widgets = {

            'team':forms.CheckboxSelectMultiple(choices = TEAM),
            'situation': forms.CheckboxSelectMultiple(choices = SITUATION),
            'player' : forms.TextInput(),
        }