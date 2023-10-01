from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import HealthProfileForm, HealthProfilePSCForm
from .models import HealthProfile

# Create your views here.

from autho.models import CustomUser
from .models import HealthProfile  
from .diet import Diet
from django.contrib import messages

@login_required
def home_view(request):
    user = request.user  # Get the currently logged-in user
    try:
        custom_user = CustomUser.objects.get(id=user.id)
        health_profile = HealthProfile.objects.get(user=user)
    except (CustomUser.DoesNotExist, HealthProfile.DoesNotExist):
        custom_user = None
        health_profile = None

    context = {
        'custom_user': custom_user,
        'health_profile': health_profile,
    }
    return render(request, 'user_dashboard.html', context)


@login_required
def health_profile(request):
    user = request.user
    try:
        health_profile = HealthProfile.objects.get(user=user)
    except HealthProfile.DoesNotExist:
        health_profile = None

    if request.method == 'POST':
        form = HealthProfileForm(request.POST, request.FILES, instance=health_profile)
        if form.is_valid():
            health_profile = form.save(commit=False)
            health_profile.user = user
            health_profile.save()

            # Redirect to the 'home' URL after successfully saving the form
            return redirect('home')
        else:
            # Form is not valid, collect errors and display them
            messages.error(request, 'Please correct the errors below.')

    else:
        form = HealthProfileForm(instance=health_profile)

    return render(request, 'health_profile.html', {'form': form})


@login_required
def diet(request):
    health_profile = None
    try:
        health_profile = HealthProfile.objects.get(user=request.user)
    except HealthProfile.DoesNotExist:
        redirect('health-profile')
    
    data = {}
    if health_profile is not None:
        diet = Diet(health_profile.height, health_profile.weight, health_profile.gender, health_profile.age)
    
        diet_plan =  diet.get_diet_plan()
    
        data = {
            # 'diet_plan': diet_plan, 
            'health_profile': diet.get_health_profile()
        }
    
        for day, plan in diet_plan.items() :
            diet_plan[day] = plan.to_dict()
            diet_plan[day]['Food'] = list(plan['Food'])
            diet_plan[day]['Quantity (g)'] = list(map(int, list(plan['Quantity (g)'])))
            data[day.lower()] = zip(diet_plan[day]['Food'], diet_plan[day]['Quantity (g)'])

    return render(request, 'diet.html', data)   



@login_required
def health_profile_psc_form(request):
    # Check if the user already has a HealthProfile
    try:
        health_profile = HealthProfile.objects.get(user=request.user)
    except HealthProfile.DoesNotExist:
        health_profile = None

    if request.method == 'POST':
        form = HealthProfilePSCForm(request.POST, instance=health_profile)
        if form.is_valid():
            # Associate the health profile with the logged-in user
            health_profile = form.save(commit=False)
            health_profile.user = request.user
            health_profile.save()
            
            return redirect('user-home')  # Redirect to a success page
    else:
        form = HealthProfilePSCForm(instance=health_profile)

    return render(request, 'health_profile_psc_form.html', {'form': form})


