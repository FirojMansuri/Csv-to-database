# forms.py
from django import forms
from .models import ModalData

class UploadFileForm(forms.ModelForm):  # Change from forms.Form to forms.ModelForm
    class Meta:
        model = ModalData
        fields = '__all__'
