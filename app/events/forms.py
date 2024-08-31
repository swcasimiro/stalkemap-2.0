from .models import ResponseEvent
from django.forms import ModelForm, TextInput
from django import forms


class ResponseEventForm(ModelForm):
    class Meta:
        model = ResponseEvent
        fields = ['faction_link', 'vk',
                  'description']
        widgets = {
            "faction_link": TextInput(attrs={
                'type': 'text',
                'required': 'required',
            }),
            "vk": TextInput(attrs={
                'type': 'text',
                'required': 'required',
            }),
            "description": TextInput(attrs={
                'type': 'text',
                'required': 'required',
            }),
        }
