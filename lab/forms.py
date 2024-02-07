from django import forms
from .models import LabUser

class LabRegistrationForm(forms.ModelForm):
    lab_email = forms.EmailField(label='Email')
    lab_password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = LabUser
        fields = ['lab_name', 'lab_owner', 'lab_email', 'lab_password', 'details']
        labels = {
            'lab_email': 'Email',
            'lab_password': 'Password',
        }





class LabLoginForm(forms.Form):
    lab_id = forms.IntegerField(label='Lab ID')
    lab_password = forms.CharField(widget=forms.PasswordInput, label='Password')
