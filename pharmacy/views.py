
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Medicine, Prescription, Order
from .forms import PrescriptionForm


def pharmacy_home(request):
    # Handle prescription upload logic here
    return render(request, 'about1.html')

def upload_prescription(request):
    # Handle prescription upload logic here
    return render(request, 'upload_prescription.html')

def order_medicine(request):
    # Handle ordering medicine logic here
    return render(request, 'order_medicine.html')

def view_cart(request):
    # Display the medicine cart and allow users to update quantities or remove items
    return render(request, 'view_cart.html')

def track_order(request, order_id):
    # Display order tracking information
    return render(request, 'track_order.html')

