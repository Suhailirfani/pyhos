from django import forms
from home.models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'address', 'phone']  # Include the relevant fields
