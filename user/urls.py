from django.urls import path
from . import views

urlpatterns = [

    path('home/', views.home_view, name='user-home'),
    path('health-profile/', views.health_profile, name='health-profile'),
    path('diet/', views.diet, name='diet'),
    path('collect-health-data/', views.health_profile_psc_form, name='collect-health-data'),

]
