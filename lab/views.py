from django.shortcuts import render, redirect
from .forms import LabRegistrationForm, LabLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def lab_registration(request):
    if request.method == 'POST':
        form = LabRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')  # Redirect to a success page or another URL
    else:
        form = LabRegistrationForm()

    return render(request, 'lab_registration.html', {'form': form})


def lab_login(request):
    if request.method == 'POST':
        form = LabLoginForm(request.POST)
        if form.is_valid():
            lab_email = form.cleaned_data['lab_email']
            lab_password = form.cleaned_data['lab_password']
            
            # Authenticate user
            user = authenticate(request, username=lab_email, password=lab_password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the lab dashboard or another URL upon successful login
            else:
                # Authentication failed
                # You can add an error message here
                pass
    else:
        form = LabLoginForm()

    return render(request, 'lab_login.html', {'form': form})
