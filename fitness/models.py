from django.db import models
from django.contrib.auth.models import User
from autho.models import CustomUser

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    health_metrics = models.TextField()

    def __str__(self):
        return self.user.email

class ActivityLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    activity_date = models.DateField()
    activity_name = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()
    activity_completed = models.BooleanField(default=False) 


    def __str__(self):
        return self.user.email

class FitnessGoal(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    goal_name = models.CharField(max_length=100)
    goal_description = models.TextField()
    target_date = models.DateField()
    is_achieved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

# class NutritionLog(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     meal_date = models.DateField()
#     meal_name = models.CharField(max_length=100)
#     calories_consumed = models.PositiveIntegerField()
#     protein_grams = models.PositiveIntegerField()
#     carbs_grams = models.PositiveIntegerField()
#     fats_grams = models.PositiveIntegerField()
    #   def __str__(self):
    #     return self.user.email

class ProgressReport(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    report_date = models.DateField()
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    body_fat_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('user', 'report_date')

    def __str__(self):
        return f"Progress Report for {self.user.username} on {self.report_date}"


class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email


