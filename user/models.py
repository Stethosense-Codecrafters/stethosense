from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model
from decimal import Decimal

User = get_user_model()

class HealthProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    allergies = models.TextField(blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Height in centimeters")
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Weight in kilograms")
    age = models.PositiveIntegerField(blank=True, null=True)
    calories = models.FloatField(blank=True, null=True, help_text="Daily calorie requirements")
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    blood_group = models.CharField(max_length=3, blank=True, null=True)
    emergency_contact = models.CharField(max_length=15, blank=True, null=True, help_text="Emergency contact number")
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True, null=True)
    emergency_contact= models.CharField(max_length=15, null=True, blank=True)
    bmi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Body Mass Index")
    blood_pressure = models.CharField(max_length=15, blank=True, null=True, help_text="Blood Pressure")
    blood_glucose = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Blood Glucose Level")
    cholesterol = models.JSONField(blank=True, null=True, help_text="Cholesterol Levels (JSON)")

    def __str__(self):
        return f"{self.user.medical_id} - {self.user.email}"
    
    def calculate_bmi(self):
        if self.height and self.weight:
            # Calculate BMI using the formula: BMI = weight (kg) / (height (m) * height (m))
            height_in_meters = Decimal(self.height) / 100
            weight_in_kg = Decimal(self.weight)
            bmi = weight_in_kg / (height_in_meters * height_in_meters)
            self.bmi = bmi
        else:
            self.bmi = None


    def save(self, *args, **kwargs):
        # Calculate calories based on gender, age, height, and weight
        if self.gender and self.age and self.height and self.weight:
            # Constants for calorie calculation
            BMR_MALE = Decimal('88.362')
            BMR_FEMALE = Decimal('447.593')
            ACTIVITY_MULTIPLIER = Decimal('1.375')  # Slightly active

            # Determine BMR based on gender
            if self.gender == 'M':
                bmr = BMR_MALE
            elif self.gender == 'F':
                bmr = BMR_FEMALE
            else:
                raise ValueError("Invalid gender. Use 'M' for Male or 'F' for Female.")

            # Convert height, weight, and age to Decimal
            height_decimal = Decimal(self.height)
            weight_decimal = Decimal(self.weight)
            age_decimal = Decimal(self.age)

            # Calculate BMR using the Mifflin-St Jeor equation
            bmr += Decimal('13.397') * weight_decimal + Decimal('4.799') * height_decimal - Decimal('5.677') * age_decimal

            # Calculate daily calorie requirements based on activity level
            self.calories = int(bmr * ACTIVITY_MULTIPLIER)
        else:
            self.calories = None
        self.calculate_bmi()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.medical_id} - {self.user.email}"
