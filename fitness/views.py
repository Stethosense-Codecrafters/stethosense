import json
from datetime import date

from django.shortcuts import render,redirect ,get_object_or_404
from .models import UserProfile, ActivityLog, FitnessGoal, ProgressReport
from .forms import UserProfileForm, ActivityLogForm, ProgressReportForm
from user.models import HealthProfile 
from django.contrib import messages  

from django.contrib.auth.decorators import login_required
from user.models import HealthProfile


def fitness_home(request):
   
    return render(request, 'fitness-home.html')

def workout_planner(request):
 
    return render(request, 'fitness-workout-planner.html')

@login_required
def fitness_dashboard(request):
    user = request.user
    
    try:
        user_profile = HealthProfile.objects.get(user=user)
        fitness_goals_data = FitnessGoal.objects.filter(user=user)
    except UserProfile.DoesNotExist:
        return redirect('fill_user_profile') 
    activity_logs = ActivityLog.objects.filter(user=user)[:5]
   
    health_metrics_data = {}

    # Include health metrics from HealthProfile
    health_metrics_data['Height'] = user_profile.height
    health_metrics_data['Weight'] = user_profile.weight
    health_metrics_data['Age'] = user_profile.age
    health_metrics_data['Calories'] = user_profile.calories
    health_metrics_data['Gender'] = user_profile.gender
    health_metrics_data['BMI'] = user_profile.bmi

    # Check if health_metrics field is available and update the dictionary
    # if user_profile.health_metrics:
    #     existing_metrics = json.loads(user_profile.health_metrics)
    #     health_metrics_data.update(existing_metrics)

    progress_reports = ProgressReport.objects.filter(user=user).order_by('-report_date')[:5]

    context = {
        'title': 'Fitness Dashboard',
        'user_profile': user_profile,
        'activity_logs': activity_logs,
        'progress_reports': progress_reports,
        'health_metrics_data': health_metrics_data,
        'fitness_goals_data': fitness_goals_data,
    }
    return render(request, 'fitness-dashboard.html', context)


@login_required  
def fill_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            fitness_goal = form.save(commit=False)  
            fitness_goal.user = request.user 
            fitness_goal.save()  
            return redirect('fitness-dashboard')  
    else:
        form = UserProfileForm()

    context = {
        'title': 'Fitness Goal Form',
        'form': form,
    }
    return render(request, 'fitness-fill-user-profile.html', context)



# def fill_user_profile(request):
#     user = request.user

#     try:
#         user_profile = UserProfile.objects.get(user=user)
#     except UserProfile.DoesNotExist:
#         user_profile = None

#     try:
#         health_profile = HealthProfile.objects.get(user=user)
#     except HealthProfile.DoesNotExist:
#         health_profile = None

#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=user_profile)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = user

#             raw_fitness_goals = request.POST.get('fitness_goals', '')
    
#             health_metrics_data = {
#                 'height': str(health_profile.height),
#                 'weight': str(health_profile.weight),
#                 'age': str(health_profile.age),
#                 'calories': str(health_profile.calories),
#                 'gender': health_profile.gender,
#                 'bmi': str(health_profile.bmi),
#                 'blood_pressure': health_profile.blood_pressure,
#                 'blood_glucose': str(health_profile.blood_glucose),
#                 'cholesterol': health_profile.cholesterol,
#             }

#             # Convert the serialized data to JSON
#             health_metrics_json = json.dumps(health_metrics_data)

#             # Store the serialized data in the health_metrics field of UserProfile
#             user_profile.health_metrics = health_metrics_json
#             fitness_goals_list = [goal.strip() for goal in raw_fitness_goals.split('\n') if goal.strip()]  
#             user_profile.fitness_goals = fitness_goals_list
#             user_profile.save()

#             return redirect('fitness-dashboard')  
#     else:
#         form = UserProfileForm(instance=user_profile)

#     context = {
#         'title': 'Fitness User Profile Form',
#         'form': form,
#     }
#     return render(request, 'fitness-fill-user-profile.html', context)



@login_required  # Use this decorator to ensure the user is logged in
def fitness_tracking(request):
    if request.method == 'POST':
        form = ActivityLogForm(request.POST)
        if form.is_valid():
            current_date = date.today()
            form.instance.activity_date = current_date
            form.instance.user = request.user  # Set the user field to the currently logged-in user
            form.save()
            return redirect('fitness-dashboard')
        else:
            # If the form is not valid, display error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")

    else:
        form = ActivityLogForm()

    return render(request, 'fitness-tracking.html', {'form': form})

@login_required
def update_fitness_goal(request, goal_id):
    goal = get_object_or_404(FitnessGoal, id=goal_id)

    if request.method == 'POST':
        if 'activity_completed' in request.POST:
            goal.is_achieved = not goal.is_achieved
            goal.save()

    return redirect('fitness-dashboard')



@login_required
def progress_reports(request):
    user = request.user

    # Retrieve progress reports for the current user
    progress_reports = ProgressReport.objects.filter(user=user).order_by('-report_date')

    context = {
        'title': 'Progress Reports',
        'progress_reports': progress_reports,
    }

    return render(request, 'fitness-progress-reports.html', context)

@login_required

def submit_progress_report(request):
    if request.method == 'POST':
        form = ProgressReportForm(request.POST)

        if form.is_valid():
            user = request.user
            report_date = form.cleaned_data['report_date']

            # Check if a progress report already exists for this user and report date
            existing_report = ProgressReport.objects.filter(user=user, report_date=report_date).first()

            if existing_report:
                # Update the existing progress report
                existing_report.weight_kg = form.cleaned_data['weight_kg']
                existing_report.body_fat_percentage = form.cleaned_data['body_fat_percentage']
                existing_report.save()
            else:
                # Create a new progress report
                new_report = form.save(commit=False)
                new_report.user = user
                new_report.save()

            return redirect('fitness-dashboard')  # Redirect to a success page or any other page you prefer
    else:
        form = ProgressReportForm()

    context = {
        'form': form,
    }
    return render(request, 'fitness-submit-progress-report.html', context)
