# office_admin/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('edit_patient/<int:patient_id>/', views.edit_patient, name='edit_patient'),
    path('edit_appointment/<int:appointment_id>/', views.edit_appointment, name='edit_appointment'),
    # path('edit_appointment/<int:appointment_id>/', views.edit_appointment, name='edit_appointment'),
    path('delete_appointment/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('manage_doctors/', views.manage_doctors, name='manage_doctors'),
    path('update_doctor_profile/<int:doctor_id>/', views.update_doctor_profile, name='update_doctor_profile'),
    path('schedule_appointment/', views.schedule_appointment, name='schedule_appointment'),
    path('appointments/', views.appointments, name='appointments'),
   
]