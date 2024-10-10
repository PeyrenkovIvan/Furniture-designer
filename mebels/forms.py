from django.forms import ModelForm , CheckboxInput
from django import forms
from .models import Bed
from django.utils.translation import gettext


class BedForm(forms.Form):
    length = forms.ChoiceField(
        choices=[
            ('200', '200'),
            ('220', '220')
        ],

        )

    width = forms.ChoiceField(
        choices=[
            ('80','80'),
            ('100','100'),
            ('200','200'),
        ],

        )

    base = forms.ChoiceField(
        choices=[
            ('Comfort', gettext('Comfort')),
            ('Prestige',gettext('Prestige')),
        ],
        label=gettext("Base"),

        )

    color = forms.ChoiceField(
        choices=[
            ('Red','Red'),
            ('Blue','Blue'),
            ('Yellow','Yellow'),
        ],

        )
    