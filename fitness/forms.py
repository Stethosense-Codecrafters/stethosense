from django import forms
from .models import UserProfile, ActivityLog, FitnessGoal, ProgressReport

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = FitnessGoal
        fields = ['goal_name', 'goal_description', 'target_date', 'is_achieved']


class ActivityLogForm(forms.ModelForm):
    class Meta:
        model = ActivityLog
        fields = ['activity_date', 'activity_name', 'duration_minutes', 'calories_burned']
        widgets = {
            'activity_date': forms.DateInput(attrs={'required': False}),
        }

class ProgressReportForm(forms.ModelForm):
    class Meta:
        model = ProgressReport
        fields = ['report_date', 'weight_kg', 'body_fat_percentage']
