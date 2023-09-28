from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserAdminCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from .models import *
from django import forms
from django. contrib import messages
from django.urls import reverse

import uuid
from user.models import HealthProfile


from django.urls import reverse_lazy

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.views import PasswordResetView


def home(request):
    user=request.user
    return render(request, 'index.html', {'user':user})

@csrf_exempt
def loginPage(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            try:
                health_profile = HealthProfile.objects.get(user=user)
                return redirect(reverse('home'))
            except HealthProfile.DoesNotExist:
                return redirect(reverse('health-profile'))
            return redirect(reverse('home'))
        else:
            messages.info(request, 'Password or Username is incorrect')
            return render(request, 'login.html')

    return render(request, 'login.html')




def signup(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Generate a 12-digit medical_id
            medical_id = str(uuid.uuid4())
            medical_id = medical_id.replace('-', '').upper()[:12]

            # Assign the medical_id to the user
            user.medical_id = medical_id
            user.save()

            username = form.cleaned_data.get('first_name')

            messages.success(request, 'Account Created for ' + str(user) + ' Please login')
            return redirect('login')
    return render(request, 'signup.html', {'form': form})




class CustomPasswordResetView(PasswordResetView):
    template_name = 'reset_password.html'

    def form_valid(self, form):
        """
        This method is called when the form is valid and the email has been sent.
        """
        messages.info(self.request, "If you have an account associated with this email, a password reset link has been sent.")
        return super().form_valid(form)




@login_required
def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # Clean the form data, including the old_password field
            form.clean()
            user = form.save()
            # Important: update the user's session to avoid logging them out
            update_session_auth_hash(request, user)
            # Show a success message
            messages.success(request, 'Password updated successfully.')
            # Redirect to the home page or any other URL you prefer
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, 'Password update failed. Please correct the errors.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'update_password.html', {'form': form})



