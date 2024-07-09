# patient/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('make_appointment/', views.make_appointment, name='make_appointment'),
    path('create_patient_profile/', views.create_patient_profile, name='create_patient_profile'),
]
