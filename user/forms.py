from django import forms
from .models import HealthProfile

GENDER_CHOICES = (
('M', 'Male'),
('F', 'Female'),
('O', 'Other'),
)

class HealthProfileForm(forms.ModelForm):    
    allergies = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 12vh'}))
    height = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    weight = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # gender = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
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

class HealthProfilePSCForm(forms.ModelForm):
    blood_pressure = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your blood pressure, e.g., "120/80 mm Hg"'},
        ),
        label='Blood Pressure'
    )

    blood_glucose = forms.DecimalField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your blood glucose level, e.g., "5.4"'},
        ),
        label='Blood Glucose Level'
    )

    cholesterol = forms.JSONField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter cholesterol levels as JSON, e.g., {"hdl": 50, "ldl": 100}'},
        )
    )

    class Meta:
        model = HealthProfile
        fields = ['blood_pressure', 'blood_glucose', 'cholesterol']


