
from django.contrib import admin
from django.urls import path, include
from excelapp.viewsedit import upload_file  # Import the upload_file view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', upload_file, name='upload_file'),  # Use the upload_file view for the root URL
]
