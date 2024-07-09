# Register your models here.
from django.contrib import admin
from . models import Doctor, Patient, Prescription, Appointment, Department, TreatmentRecord, Billing, OfficeAdmin
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Prescription)
admin.site.register(Appointment)
admin.site.register(Department)
admin.site.register(TreatmentRecord)
admin.site.register(Billing)
admin.site.register(OfficeAdmin)