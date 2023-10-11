from django import forms
from django.contrib.auth.models import User                    #its a model that defines the parameters of a user
from django.contrib.auth.forms import UserCreationForm


from django import forms
from .models import Prescription

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['prescription_file']

    def clean_prescription_file(self):
        prescription_file = self.cleaned_data.get('prescription_file')

        # Ensure the uploaded file is a valid prescription file (you can add more validation here)
        if prescription_file:
            file_extension = prescription_file.name.split('.')[-1].lower()
            if file_extension not in ['pdf', 'jpg', 'jpeg', 'png']:
                raise forms.ValidationError('Invalid file format. Please upload a PDF, JPG, or PNG file.')

        return prescription_file
