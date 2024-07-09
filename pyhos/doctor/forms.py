from django import forms
from home.models import Doctor

class TimeInput(forms.TimeInput):
    input_type = 'time'


class DoctorAvailabilityForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [ 'availability_start', 'availability_end']
        widgets = {
            'availability_start' : TimeInput(),
            'availability_end': TimeInput(),
        }


class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization', 'department', 'image']


