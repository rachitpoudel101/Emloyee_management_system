from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import EmployeeDetails
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def registration(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST.get('firstname')
        ln = request.POST.get('lastname')
        ecode = request.POST.get('employeecode')
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        try:
            # Create the user
            user = User.objects.create_user(first_name=fn, last_name=ln, username=email, password=pwd)
            # Create the employee details entry
            EmployeeDetails.objects.create(user=user, empcode=ecode)
            error = "no"
            return redirect('emp_login')
        except Exception as e:
            error = "yes"
            print(e)  # Log the exception for debugging purposes
    context = {'error': error}
    return render(request, 'registration.html', context)

@login_required(login_url='emp_login')
def profile(request):
    error = ""
    user = request.user
    employee = get_object_or_404(EmployeeDetails, user=user)

    if request.method == 'POST':
        fn = request.POST.get('firstname')
        ln = request.POST.get('lastname')
        ecode = request.POST.get('employeecode')
        email = request.POST.get('emailid')
        contact = request.POST.get('contact')
        department = request.POST.get('department')
        designation = request.POST.get('designation')
        joining_date = request.POST.get('Jdate')
        gender = request.POST.get('gender')
        
        try:
            # Update the user's details
            user.first_name = fn
            user.last_name = ln
            user.email = email
            user.save()
            
            # Update the employee details
            employee.empcode = ecode
            employee.contact = contact
            employee.empdept = department
            employee.designation = designation
            employee.joiningdate = joining_date  
            employee.gender = gender
            employee.save()
            
            error = "no"
        except Exception as e:
            error = "yes"
            print(e)  # Log the exception for debugging purposes
    
    context = {'error': error, 'employee': employee}
    return render(request, 'profile.html', context)

def emp_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('emp_home')
        else:
            error = "yes"
    context = {'error': error}
    return render(request, 'login.html', context)

@login_required(login_url='emp_login')
def emp_home(request):
    return render(request, 'emp_home.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def admin_login(request):
    return render(request, 'admin_login.html')
