# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Add this import
from .forms import ExcelUploadForm
import pandas as pd

@csrf_exempt  # Add this decorator to exempt CSRF for testing (for production, use a proper csrf token handling)
def upload_file(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            tfms_file = form.cleaned_data['tfms_file']
            wbu_file = form.cleaned_data['wbu_file']

            total_booking_hours = calculate_total_booking_hours(tfms_file) if tfms_file else None
            total_utilized_hours = calculate_total_utilized_hours(wbu_file) if wbu_file else None

            return JsonResponse({
                'total_booking_hours': total_booking_hours,
                'total_utilized_hours': total_utilized_hours,
            })
    else:
        form = ExcelUploadForm()

    return render(request, 'upload.html', {'form': form})

def calculate_total_booking_hours(tfms_file):
    if tfms_file:
        df = pd.read_excel(tfms_file, skiprows=3)
        #if 'endTime' in df.columns and 'startTime' in df.columns:
        total_booking_hours = (df['endTime'] - df['startTime']).sum().total_seconds() / 3600
        return total_booking_hours
        #else:
            #return None
    return None

def calculate_total_utilized_hours(wbu_file):
    if wbu_file:
        df = pd.read_excel(wbu_file, skiprows=2)
        total_utilized_hours = df['Automation'].add(df['Manual']).sum()
        return total_utilized_hours
    return None
