from django.urls import path
from . import views

urlpatterns = [
    path('lab-registration/', views.lab_registration, name='lab_registration'),
    path('lab-login/', views.lab_login, name='lab_login'),
]
