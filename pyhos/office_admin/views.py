# Create your views here.
# office_admin/views.py
from django.shortcuts import render, redirect,get_object_or_404
from home.models import Appointment
from django.contrib.auth.decorators import login_required
from .forms import PatientForm, AppointmentForm

@login_required
def admin_dashboard_appointment(request):
    appointments = Appointment.objects.all()
    return render(request, 'admin_dashboard.html', {'appointments': appointments})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import Appointment ,Patient, Doctor

@login_required
def admin_dashboard(request):
    # Get quick statistics
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_appointments = Appointment.objects.count()
    # total_supplies = MedicalSupply.objects.count()
    patients = Patient.objects.all()
    recent_appointments = Appointment.objects.order_by('-appointment_date')[:10]
    # recent_admissions = Admission.objects.order_by('-admitted_on')[:10]
    
    # # Recent activities
    # recent_appointments = Appointment.objects.order_by('-date')[:5]
    # recent_admissions = Patient.objects.order_by('-admitted_on')[:5]
    
    context = {
        'total_patients': total_patients,
        'patients':patients,
        'total_doctors': total_doctors,
        'total_appointments': total_appointments,
        #  'total_supplies': total_supplies,
        'recent_appointments': recent_appointments,
        # 'recent_admissions': recent_admissions,
    }
    return render(request, 'admin/office_admin_dashboard.html', context)


def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PatientForm()
    return render(request, 'admin/add_patient.html', {'form': form})

def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'admin/edit_patient.html', {'form': form})

# def edit_appointment(request, appointment_id):
#     appointment = get_object_or_404(Appointment, pk=appointment_id)
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST, instance=appointment)
#         if form.is_valid():
#             form.save()
#             return redirect('admin/office_admin_dashboard')
#     else:
#         form = AppointmentForm(instance=appointment)
#     return render(request, 'admin/edit_appointment.html', {'form': form})
from django.shortcuts import render, get_object_or_404

from django.urls import reverse
def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    # Handle the editing logic here
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
           
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'admin/edit_appointment.html', {'form': form})


# def some_view(request):
#     # Your logic here
#     return redirect(reverse('edit_appointment', args=[appointment_id]))


def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointments')
    return render(request, 'admin/delete_appointment.html', {'appointment': appointment})

# def delete(request,pk):
#     instance=BookInfo.objects.get(pk=pk)
#     instance.delete()
#     book_set=BookInfo.objects.all()
#     return render(request,'list.html',{'books':book_set})

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from home.models import Doctor, Appointment
from home.forms import DoctorForm, AppointmentForm

@login_required
def manage_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'admin/manage_doctors.html', {'doctors': doctors})

@login_required
def update_doctor_profile(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('manage_doctors')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'admin/update_doctor_profile.html', {'form': form, 'doctor': doctor})

@login_required
def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments')
    else:
        form = AppointmentForm()
    return render(request, 'admin/schedule_appointment.html', {'form': form})


@login_required
def appointments(request):
    # Fetch all appointments for the logged-in user
    # patient = request.user.patient
    # user_appointments = Appointment.objects.filter(patient__user=request.user)
    # return render(request, 'appointments.html', {'appointments': user_appointments}, patient)
    from home.models import Appointment, Patient

@login_required
def appointments(request):
    try:
        patient = request.user.patient
    except Patient.DoesNotExist:
        # Redirect to a view where user can create a patient profile
        return redirect('appointment_success')

    appointments = Appointment.objects.filter(patient=patient)
    return render(request, 'appointments.html', {'appointments': appointments})
