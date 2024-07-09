from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render, get_object_or_404

# Create your views here.
# doctor/views.py
from home.models import Appointment, Prescription, Doctor
from django.contrib.auth.decorators import login_required

@login_required
def doctor_dashboard(request):
    appointments = Appointment.objects.filter(doctor__user=request.user)
    doctors = request.user.userprofile
    return render(request, 'doctor/doctor_dashboard.html', {'appointments': appointments, 'doctors':doctors})

@login_required
def write_prescription(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        prescription_text = request.POST['prescription_text']
        Prescription.objects.create(appointment=appointment, prescription_text=prescription_text)
        return redirect('doctor_dashboard')
    return render(request, 'doctor/write_prescriptions.html', {'appointment': appointment})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DoctorAvailabilityForm

@login_required
def update_availability(request):
    doctor = request.user.doctor
    if request.method == 'POST':
        form = DoctorAvailabilityForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_dashboard')
    else:
        form = DoctorAvailabilityForm(instance=doctor)
    return render(request, 'doctor/update_availability.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DoctorProfileForm

@login_required
def update_profile(request):
    doctor = request.user.userprofile.doctor
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_dashboard')
    else:
        form = DoctorProfileForm(instance=doctor)
    return render(request, 'doctor/update_profile.html', {'form': form})
