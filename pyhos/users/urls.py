from . import views

from django.contrib import admin
from django.urls import  path

urlpatterns = [
    path('login_selection/', views.login_selection, name='login_selection'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('login/admin/', views.admin_login, name='admin_login'),
    path('login/doctor/', views.doctor_login, name='doctor_login'),
    path('login/patient/', views.patient_login, name='patient_login'),

]