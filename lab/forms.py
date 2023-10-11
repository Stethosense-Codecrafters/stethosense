from django import forms
from .models import LabReport

class LabReportForm(forms.ModelForm):
    class Meta:
        model = LabReport
        fields = ['report_name', 'report_file', 'description', 'price', 'lab_name', 'doctor_name', 'lab_location', 'test_type', 'is_verified']
