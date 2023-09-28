from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model

User = get_user_model()

class HealthProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    allergies = models.TextField(blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Height in centimeters")
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Weight in kilograms")
    age = models.PositiveIntegerField(blank=True, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    blood_group = models.CharField(max_length=3, blank=True, null=True)
    emergency_contact = models.CharField(max_length=15, blank=True, null=True, help_text="Emergency contact number")
    profile_picture = models.ImageField(upload_to='health_profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.medical_id} - {self.user.email}"
