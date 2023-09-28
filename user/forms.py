from django import forms
from .models import HealthProfile

class HealthProfileForm(forms.ModelForm):
    allergies = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 12vh'}))
    height = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    weight = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    blood_group = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    emergency_contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = HealthProfile
        fields = [
            'allergies',
            'height',
            'weight',
            'age',
            'gender',
            'blood_group',
            'emergency_contact',
            'profile_picture',
        ]
