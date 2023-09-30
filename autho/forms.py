from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
# from django.forms import ModelForm
# from .models import CustomUser
# from django.db import models

# from django.forms.widgets import FileInput



class UserAdminCreationForm(UserCreationForm):

    """
    A Custom form for creating new users.
    """
    style = "border-radius: 8px; border: 1px lightgrey solid"
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-box', 
        'placeholder': 'First Name',
        'style': style
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-box', 'placeholder': 'Last Name', 'style': style}))

    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control text-box', 'placeholder': 'Mobile', 'style': style}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control text-box', 'placeholder': 'Email', 'style': style}))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control text-box', 'placeholder': 'Password', 'style': style}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control text-box', 'placeholder': 'Confirm Password', 'style': style}))

    class Meta:    
        model = get_user_model()
        fields = ['first_name', 'last_name', 'mobile', 'email', 'password1', 'password2']

