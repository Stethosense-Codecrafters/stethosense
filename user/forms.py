from django import forms
from .models import HealthProfile

class HealthProfileForm(forms.ModelForm):
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
