from django.contrib.auth import views as auth_views
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import DeleteAccountView


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('login/forgot/', views.forgot, name='forgot'),
    path('login/update-password/', views.update_password, name='update-password'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('delete-account/', DeleteAccountView.as_view(), name='delete_account'),
    path('account-deleted/', views.account_deleted_view, name='account_deleted'),  # Create this view



]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
