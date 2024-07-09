from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('write_prescription/<int:appointment_id>/', views.write_prescription, name='write_prescription'),
    path('update_availability', views.update_availability, name='update_availability')
]