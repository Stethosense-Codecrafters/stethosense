from django.contrib import admin
from .models import UserProfile, ActivityLog, FitnessGoal, ProgressReport, Notification



admin.site.register(UserProfile)
admin.site.register(ActivityLog)
admin.site.register(FitnessGoal)
admin.site.register(ProgressReport)
admin.site.register(Notification)
