from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import HealthProfileForm
from .models import HealthProfile

# Create your views here.

from autho.models import CustomUser
from .models import HealthProfile  

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
    return render(request, 'dashboard.html', context)




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
        form = HealthProfileForm(instance=health_profile)

    return render(request, 'health_profile.html', {'form': form})

@login_required
def diet(request) :
    # user = request.user
    
    
    return render(request, 'diet.html')