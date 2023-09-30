from django.shortcuts import render

def doctor_home(request):
    # Your view logic goes here
    # You can fetch data from models, perform calculations, etc.

    # Example: Rendering a template
    return render(request, 'doctor/doctor_home.html')
