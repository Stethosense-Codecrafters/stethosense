from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from autho.models import CustomUser  # Import your CustomUser model

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'mobile', 'medical_id')}),  # Include 'medical_id' here
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'mobile', 'email', 'password1', 'password2', 'medical_id'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'mobile', 'medical_id')  # Include 'medical_id' here
    search_fields = ('email', 'first_name', 'last_name', 'medical_id')  # Include 'medical_id' here in search fields
    ordering = ('email',)

# Register your CustomUser model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)

def __str__(self):
    return self.email
