from django.contrib.auth import forms as auth_forms
from django import forms


class AuthenticationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "form-control",
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'autocomplete': "current-password",
        })
    )


class RegistrationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "form-control",
        }),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "form-control",
        }),
        required=False,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'required': False,
        }),
        required=False,
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'class': "form-control",
        }),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
        }),
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
        })
    )
