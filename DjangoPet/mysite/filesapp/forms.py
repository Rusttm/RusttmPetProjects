from django import forms
from .models import DocumentUploaded
from django.forms import ModelForm

class DocumentForm(forms.Form):
    upload = forms.FileField(
        label='Select a file',
        # help_text='max. 4 megabytes'
    )

class DocumentModelForm(ModelForm):
    """
    make form from model DocumentUploaded
    https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#django.forms.ModelForm
    """
    class Meta:
        model = DocumentUploaded
        fields = ['upload']
