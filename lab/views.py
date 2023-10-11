from django.shortcuts import render, redirect
from .forms import LabReportForm
from django.contrib.auth.decorators import login_required


def add_lab_report(request):
    if request.method == 'POST':
        form = LabReportForm(request.POST, request.FILES)
        if form.is_valid():
            lab_report = form.save(commit=False)
            lab_report.user = request.user  # Assign the current user
            lab_report.save()
            return redirect('lab_report_list')  # Redirect to a success page or report list
    else:
        form = LabReportForm()
    return render(request, 'lab_report_form.html', {'form': form})



@login_required  # Ensure that only logged-in users can access this view
def lab_details(request):
    lab = Lab.objects.get(user=request.user)  # Assuming user is related to Lab model
    return render(request, 'labapp/lab_details.html', {'lab': lab})