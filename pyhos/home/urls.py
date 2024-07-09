from . import views

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.make_appointment, name='booking'),
    # path('departments/', views.departments, name='departments'),
    path('contact/', views.contact, name='contact'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('departments/', views.department_list, name='department_list'),
    path('doctor/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('appointment/success/', views.appointment_success, name='appointment_success'),
]