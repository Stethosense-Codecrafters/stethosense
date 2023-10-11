
from django.db import models
from autho.models import CustomUser
from django.conf import settings

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Prescription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    prescription_file = models.FileField(upload_to='prescriptions/')
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    medicines = models.ManyToManyField(Medicine, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
