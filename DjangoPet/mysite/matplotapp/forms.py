from django import forms
from matplotapp.models import Equations

class UploadFunction(forms.Form):
    function_string = forms.CharField(max_length=50)
