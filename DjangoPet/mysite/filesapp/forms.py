from django import forms
class DocumentForm(forms.Form):
    upload = forms.FileField(
        label='Select a file',
        # help_text='max. 4 megabytes'
    )