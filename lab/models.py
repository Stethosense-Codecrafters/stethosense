from django.db import models
from autho.models import CustomUser

class LabReport(models.Model):
    lab_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    report_name = models.CharField(max_length=100)
    report_date = models.DateField()
    report_file = models.FileField(upload_to='lab_reports/')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    lab_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    lab_location = models.CharField(max_length=100)
    test_type = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.report_name
