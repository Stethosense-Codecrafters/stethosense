from django.db import models
from autho.models import CustomUser

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _




# Define choices for the lab_name field
LAB_REPORT_CHOICES = (
    ('Report 1', 'Report 1'),
    ('Report 2', 'Report 2'),
    ('Report 3', 'Report 3'),
    # Add more choices as needed
)




class LabUser(AbstractUser):
    lab_id = models.BigAutoField(primary_key=True)  # Change the ID field name to lab_id
    lab_name = models.CharField(max_length=100)
    lab_owner = models.CharField(max_length=100)
    lab_email = models.EmailField(max_length=255, unique=True)
    lab_password = models.CharField(max_length=128)
    details = models.TextField(blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='lab_users_groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='lab_users_permissions'
    )




class LabReport(models.Model):
    lab = models.ForeignKey(LabUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, choices=LAB_REPORT_CHOICES)
    description = models.TextField()
    date = models.DateField()
    results = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    lab_report = models.FileField(upload_to='lab_reports/')
    
    # Additional fields for lab management
    lab_technician = models.CharField(max_length=100, null=True)  # Technician who conducted the lab test
    lab_location = models.CharField(max_length=100, null=True)  # Location or department of the lab
    lab_test_type = models.CharField(max_length=100, null=True)  # Type of lab test (e.g., blood test, urine test)
    lab_reference_range = models.CharField(max_length=100, null=True)  # Reference range for lab results
    is_urgent = models.BooleanField(default=False)  # Mark if the lab test is urgent
    is_confidential = models.BooleanField(default=False)  # Mark if the lab result is confidential

    def __str__(self):
        return self.name
