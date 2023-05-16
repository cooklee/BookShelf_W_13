from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        cleaned_data = super().clean()


        user = authenticate(**cleaned_data)
        if user is None:
            raise ValidationError('niepoprawne dane logowania')
        cleaned_data['user'] = user
        return cleaned_data

