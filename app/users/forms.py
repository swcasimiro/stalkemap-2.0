from events.models import Events, ResponseEvent
from django.forms import ModelForm, TextInput, Textarea, \
    Select, CheckboxInput, PasswordInput, EmailInput
from django import forms
from .models import Users


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )
    username = forms.CharField(
        label='Ваш никнейм',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    email = forms.CharField(
        label='Ваша почта',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
        })
    )

    class Meta:
        model = Users
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']


class LoginUserForm(forms.Form):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }
        )
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }
        )
    )


class EventForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields["type_event"].choices = [("", "Тип мероприятия"), ] + list(
            self.fields["type_event"].choices)[0:]

    class Meta:
        model = Events
        fields = ['name', 'description',
                  'type_event', 'vk',
                  'full_description', 'property',
                  'nickname']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
            }),
            "type_event": Select(attrs={
                'class': 'form-select',
            }),
            "vk": TextInput(attrs={
                'class': 'form-control',
            }),
            "full_description": Textarea(attrs={
                'class': 'form-control',
            }),
            "property": Textarea(attrs={
                'class': 'form-control',
            }),
            "nickname": TextInput(attrs={
                'class': 'form-control',
            }),
        }


class ResponseEventUpdateForm(ModelForm):
    class Meta:
        model = ResponseEvent
        fields = ['user', 'antispam']
        widgets = {
            "antispam": CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }


class ResponseEventArchiveUpdateForm(ModelForm):
    class Meta:
        model = ResponseEvent
        fields = ['user', 'archive']


class EventsArchiveUpdateForm(ModelForm):
    class Meta:
        model = ResponseEvent
        fields = ['user', 'archive']


class EventsUpdateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EventsUpdateForm, self).__init__(*args, **kwargs)
        self.fields["type_status"].choices = [("", "Выберите окончательный статус заявки"), ] + list(
            self.fields["type_status"].choices)[1:]

    class Meta:
        model = Events
        fields = ['type_status', 'description_status']
        widgets = {
            "description_status": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий к заявке...'
            }),
            "type_status": Select(attrs={
                'class': 'form-select',
            }),
        }
