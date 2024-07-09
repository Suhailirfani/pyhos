# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login as lgn, logout as lgt, authenticate
from django.db import IntegrityError

# Create your views here.
# In users/views.py
from .models import UserProfile
from django.db import transaction

def signup(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']
        
        try:
            # Check if the user already exists
            user = User.objects.create_user(username=username, password=password)
            user.save()
            
            # Create the user profile
            profile = UserProfile.objects.create(user=user, user_type=user_type)
            profile.save()
            
            user = authenticate(username=username, password=password)
            if user is not None:
                lgn(request, user)
                if user_type == 'office_admin':
                    return redirect('office_admin_dashboard')
                elif user_type == 'doctor':
                    return redirect('doctor_dashboard')
                elif user_type == 'patient':
                    return redirect('patient_dashboard')
                else:
                    error_message = 'User type not recognized'
            else:
                error_message = 'Authentication failed'
        
        except IntegrityError:
            error_message = 'Username already exists'
        
        except Exception as e:
            error_message = str(e)

    return render(request, 'users/signup.html', {'error_message': error_message})

def login(request):
    error_message = None
    if request.POST:
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user:
            lgn(request, user)
            user_type = user.userprofile.user_type
            if user_type == 'office_admin':
                return redirect('admin_dashboard')
            elif user_type == 'doctor':
                return redirect('doctor_dashboard')
            elif user_type == 'patient':
                return redirect('patient_dashboard')
            else:
                error_message = 'User type not recognized'
            return render(request, 'dashboard.html')
        else:
            error_message = 'Invalid Credentials'
    return render(request, 'users/login.html', {'error_message':error_message})    

def login_selection(request):
    return render(request, 'login_selection.html')    

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as lgn
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def admin_login(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.userprofile.user_type == 'office_admin':
                lgn(request, user)
                return redirect('admin_dashboard')
            else:
                error_message = 'This login page is for admins only.'
        else:
            error_message = 'Invalid credentials'
    return render(request, 'users/admin_login.html', {'error_message': error_message})



# def admin_login(request):
#     # Implement your admin login logic here
#     return render(request, 'users/admin_login.html')

def doctor_login(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.userprofile.user_type == 'doctor':
                lgn(request, user)
                return redirect('doctor_dashboard')
            else:
                error_message = 'This login page is for doctors only.'
        else:
            error_message = 'Invalid credentials'
    return render(request, 'users/doctor_login.html', {'error_message': error_message})


# def doctor_login(request):
#     # Implement your doctor login logic here
#     return render(request, 'users/doctor_login.html')


def patient_login(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.userprofile.user_type == 'patient':
                lgn(request, user)
                return redirect('patient_dashboard')
            else:
                error_message = 'This login page is for patients only.'
        else:
            error_message = 'Invalid credentials'
    return render(request, 'users/patient_login.html', {'error_message': error_message})

# def patient_login(request):
    # Implement your patient login logic here
    # return render(request, 'users/patient_login.html')


def logout(request):
    lgt(request)
    return redirect('login_selection')

