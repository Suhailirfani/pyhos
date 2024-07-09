from django import forms
from home.models import Patient, Appointment

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'dob', 'address', 'phone', 'email', 'medical_history']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'medical_history': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'appointment_date', 'time', 'symptoms']
