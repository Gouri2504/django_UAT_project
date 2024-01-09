# forms.py
from django import forms

class ExcelUploadForm(forms.Form):
    tfms_file = forms.FileField(label='TFMS File', required=False)
    wbu_file = forms.FileField(label='WBU File', required=False)
