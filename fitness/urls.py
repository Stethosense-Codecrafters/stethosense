from django.urls import path
from . import views

urlpatterns = [
    #path('fitness/', views.fitness_dashboard, name='fitness_dashboard'),
    path('fitness/', views.fitness_dashboard, name='fitness_dashboard'),
    path('fitness/workout/', views.workout_planner, name='workout_planner'),
]
