from django import forms
from .models import LabRegistration

class LabRegistrationForm(forms.ModelForm):
    class Meta:
        model = LabRegistration
        fields = ['lab_name', 'lab_owner', 'lab_email', 'lab_password', 'details']


class LabLoginForm(forms.Form):
    lab_email = forms.EmailField(label='Email')
    lab_password = forms.CharField(label='Password', widget=forms.PasswordInput)
