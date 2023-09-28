from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('home/', views.home_view, name='user-home'),
    path('health-profile/', views.health_profile, name='health-profile'),
    path('diet/', views.diet, name='diet')
    # ... other URL patterns ...
]
