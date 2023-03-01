from django import forms
from main.models import ContactRequest


class ContactRequestForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "Name",
    }))
    email_id = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "Email ID",
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "Phone No.",
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': "form-control",
        'placeholder': "Type your message here...",
        'rows': "9",
    }))

    class Meta:
        fields = ('name', 'email_id', 'phone', 'message')
        model = ContactRequest
