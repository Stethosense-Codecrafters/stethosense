from django.urls import path
from . import views

urlpatterns = [
    path('fitness/', views.fitness_home, name='fitness-home'),
    path('fitness/workout/', views.workout_planner, name='workout_planner'),
    path('fitness-dashboard/', views.fitness_dashboard, name='fitness-dashboard'),
    path('fitness-user-profile/', views.fill_user_profile, name='fitness-user-profile'),
    path('fitness-update-goal/<int:goal_id>/', views.update_fitness_goal, name='update-fitness-goal'),
    path('fitness-tracking/', views.fitness_tracking, name='fitness-tracking'),
    path('progress-reports/', views.progress_reports, name='progress-reports'),
    path('submit_progress_report/', views.submit_progress_report, name='submit_progress_report'),
    # path('settings-and-preferences/', views.settings_and_preferences, name='settings-and-preferences'),
]
