from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('add_lab_report/', views.add_lab_report, name='add_lab_report'),
    path('lab_details/', views.lab_details, name='lab_details'),


]
