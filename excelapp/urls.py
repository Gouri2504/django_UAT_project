# urls.py
from django.urls import path
from .viewsedit import upload_file,analysis_plot

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
     path('analysis_plot/', analysis_plot, name='analysis_plot'),
    # Add other URLs as needed
]
