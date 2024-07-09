from django.shortcuts import redirect, render


# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Doctor, Department, Appointment, Patient
from .forms import AppointmentForm, PatientAppointmentForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors})

# def booking(request):
#     return render(request, 'appo.html' )


from django.contrib.auth.decorators import login_required


# def booking(request):
#     doctors = Doctor.objects.all()
#     if request.method == 'POST':
#         doctor_id = request.POST['doctor_id']
#         date = request.POST['date']
#         time = request.POST['time']
#         symptoms = request.POST['symptoms']
#         doctor = get_object_or_404(Doctor, id=doctor_id)
#         patient = request.user.patient
#         Appointment.objects.create(doctor=doctor, patient=patient, date=date, time=time, symptoms=symptoms)
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
            if not Appointment.objects.filter(doctor=appointment.doctor, appointment_date=appointment.appointment_date, time=appointment.time).exists():
                appointment.save()
                return redirect('appointments')
            else:
                form.add_error(None, 'The doctor is not available at this time.')
    else:
        form = PatientAppointmentForm()
    return render(request, 'patient/appo.html', {'form': form , 'doctors': doctors})



def departments(request):
    return render(request, 'department.html')

def contact(request):
    return render(request, 'contact.html')

def department_list(request):
    dict_dept={
        'departments' : Department.objects.all()
    }
    return render(request, 'department.html', dict_dept )

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('appointment_success'))
    else:
        form = AppointmentForm(initial={'doctor': doctor})
    return render(request, 'doctor_detail.html', {'doctor': doctor, 'form': form})

def appointment_success(request):
    return render(request, 'appointment_success.html')
