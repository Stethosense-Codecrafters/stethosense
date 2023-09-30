from django.urls import path
from . import views

urlpatterns = [
    path('doctor/', views.doctor_home, name='doctor_home'),
    # Add more URL patterns for the "doctor" app as needed
]
