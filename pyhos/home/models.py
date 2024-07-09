from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return  self.name

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctors/')
    availability_start = models.TimeField(null=True)
    availability_end = models.TimeField(null=True)

    def __str__(self):
        return self.name
    
    def is_available(self, appointment_date):
        appointment_time = appointment_date.time()
        return self.availability_start <= appointment_time <= self.availability_end
    
    
class OfficeAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Patient(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500, null=True)
    phone = models.CharField(max_length=10,null=True)
    dob = models.DateField(null=True)
    email = models.EmailField()
    medical_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    time = models.TimeField(null=True)
    symptoms = models.TextField(blank=True)

    def __str__(self):
        return f"Appointment with {self.doctor} on {self.appointment_date} at {self.time}"

class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    prescription_text = models.TextField()

    def __str__(self):
        return f"Prescription for {self.appointment}"
    
class TreatmentRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatments = models.TextField()

class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_fee = models.DecimalField(max_digits=10, decimal_places=2)
    lab_fee = models.DecimalField(max_digits=10, decimal_places=2)
    pharmacy_fee = models.DecimalField(max_digits=10, decimal_places=2)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)



