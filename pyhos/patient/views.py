from django.shortcuts import redirect, render
from home.forms import AppointmentForm, PatientAppointmentForm

# Create your views here.
# patient/views.py
from django.shortcuts import render, get_object_or_404
from home.models import Appointment, Doctor, Prescription, Patient
from django.contrib.auth.decorators import login_required

@login_required
def patient_dashboard(request):
    appointments = Appointment.objects.filter(patient__user=request.user)
    prescriptions = Prescription.objects.filter(appointment__patient__user=request.user)
    return render(request, 'patient_dashboard.html', {'appointments': appointments, 'prescriptions': prescriptions})

# @login_required
# def make_appointment(request):
#     doctors = Doctor.objects.all()
#     patient = Patient.objects.all()
#     if request.method == 'POST':
#         doctor_id = request.POST['doctor_id']
#         date = request.POST['date']
#         time = request.POST['time']
#         symptoms = request.POST['symptoms']
#         doctor = get_object_or_404(Doctor, id=doctor_id)
#         patient = request.user.patient
#         Appointment.objects.create(doctor=doctor, patient=patient, appointment_date=date, time=time, symptoms=symptoms)
#         return redirect('patient_dashboard')
#     return render(request, 'patient/appo.html', {'doctors': doctors})

@login_required
def make_appointment(request):
    doctors = Doctor.objects.all()
    try:
        patient = request.user.patient
    except Patient.DoesNotExist:
        return redirect('create_patient_profile')

    if request.method == 'POST':
        form = PatientAppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.save()
            return redirect('appointments')
    else:
        form = PatientAppointmentForm()
    return render(request, 'patient/appo.html', {'form': form ,  'doctors': doctors })


from django.contrib.auth.decorators import login_required
from .forms import PatientForm

@login_required
def create_patient_profile(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user
            patient.save()
            return redirect('make_appointment')
    else:
        form = PatientForm()
    return render(request, 'patient/create_patient_profile.html', {'form': form})
