from django.shortcuts import render, redirect
from .forms import LabRegistrationForm, LabLoginForm
from .models import LabUser, LabReport
from django.contrib.auth import authenticate, login
import random

def generate_lab_id():
    # Generate a random 6-digit lab ID
    return random.randint(100000, 999999)

def lab_registration(request):
    if request.method == 'POST':
        form = LabRegistrationForm(request.POST)
        if form.is_valid():
            # Generate a 6-digit lab ID
            lab_id = generate_lab_id()
            form.instance.lab_id = lab_id

            # Save the form with the lab ID
            lab = form.save()

            # You might want to log in the lab immediately after registration if required
            login(request, lab)

            return redirect('about')  # Redirect to a success page or another URL
    else:
        form = LabRegistrationForm()

    return render(request, 'lab_registration.html', {'form': form})

def lab_login(request):
    error_message = None

    if request.method == 'POST':
        form = LabLoginForm(request.POST)
        if form.is_valid():
            lab_id = form.cleaned_data['lab_id']
            lab_password = form.cleaned_data['lab_password']

            # Authenticate the lab using id and password
            lab = authenticate(request, lab_id=lab_id, lab_password=lab_password)

            if lab is not None:
                # Login the lab
                login(request, lab)
                return redirect('home')  # Replace 'dashboard' with your actual dashboard URL
            else:
                error_message = "Invalid lab ID or password. Please try again."
        else:
            error_message = "Invalid form data. Please correct the errors."
    else:
        form = LabLoginForm()

    context = {
        'form': form,
        'error_message': error_message,
    }

    return render(request, 'lab_login.html', context)




def lab_dashboard(request):
    # Assuming the user is logged in and you have access to the LabUser instance
    lab_user = request.user

    # Query the database to get all lab reports associated with the lab user
    lab_reports = LabReport.objects.filter(lab=lab_user)

    context = {
        'user': lab_user,
        'lab_reports': lab_reports,
    }

    return render(request, 'lab_dashboard.html', context)
