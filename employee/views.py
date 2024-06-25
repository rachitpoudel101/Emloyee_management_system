from pyexpat.errors import messages
from django.contrib.auth import logout
from django.contrib.auth import login, logout as logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import EmployeeDetails, EmployeeExperience, EmployeeEducation


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
        
        # Validate form data
        if not all([fn, ln, ecode, email, pwd]):
            context = {'error': 'All fields are required'}
            return render(request, 'registration.html', context)
        
        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=email, email=email, password=pwd)
            EmployeeDetails.objects.create(user=user, empcode=ecode)
            EmployeeExperience.objects.create(user=user)
            EmployeeEducation.objects.create(user=user)
            return redirect('emp_login')
        except IntegrityError:
            context = {'error': 'Integrity error occurred. Possibly due to duplicate entries or database constraints.'}
        except Exception as e:
            context = {'error': 'An error occurred during registration. Please try again.'}
            print(f"Exception: {e}")
        return render(request, 'registration.html', context)
    
    return render(request, 'registration.html', {'error': error})

@login_required(login_url='emp_login')
def profile(request):
    error = ""
    user = request.user
    employee, created = EmployeeDetails.objects.get_or_create(user=user)

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
            user.first_name = fn
            user.last_name = ln
            user.email = email
            user.save()

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
            print(f"Exception: {e}")

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

@login_required(login_url='emp_login')
def my_experience(request):
    user = request.user
    try:
        experience = get_object_or_404(EmployeeExperience, user=user)
        context = {'experience': experience}
        return render(request, 'my_experience.html', context)
    except Exception as e:
        print(f"Exception: {e}")
        return render(request, 'my_experience.html', {'error': 'Could not retrieve experience details.'})

@login_required(login_url='emp_login')
def edit_my_experience(request):
    error = ""
    user = request.user

    experience, created = EmployeeExperience.objects.get_or_create(user=user)

    if request.method == 'POST':
        company1name = request.POST.get('company1name')
        company1desig = request.POST.get('company1desig')
        company1salary = request.POST.get('company1salary')
        company1duration = request.POST.get('company1duration')
        company2name = request.POST.get('company2name')
        company2desig = request.POST.get('company2desig')
        company2salary = request.POST.get('company2salary')
        company2duration = request.POST.get('company2duration')

        try:
            experience.company1name = company1name
            experience.company1desig = company1desig
            experience.company1salary = company1salary
            experience.company1duration = company1duration
            experience.company2name = company2name
            experience.company2desig = company2desig
            experience.company2salary = company2salary
            experience.company2duration = company2duration
            experience.save()

            error = "no"
        except Exception as e:
            error = "yes"
            print(f"Exception: {e}")

    context = {'error': error, 'experience': experience}
    return render(request, 'edit_exp.html', context)

@login_required(login_url='emp_login')
def my_education(request):
    user = request.user
    try:
        education = get_object_or_404(EmployeeEducation, user=user)
        context = {'education': education}
        return render(request, 'my_education.html', context)
    except Exception as e:
        print(f"Exception: {e}")
        return render(request, 'my_education.html', {'error': 'Could not retrieve education details.'})

@login_required(login_url='emp_login')
def edit_myeducation(request):
    error = ""
    user = request.user

    education, created = EmployeeEducation.objects.get_or_create(user=user)

    if request.method == 'POST':
        coursepg = request.POST.get('coursepg')
        schoolcolgpg = request.POST.get('schoolcolgpg')
        yearofpassingpg = request.POST.get('yearofpassingpg')
        percentagepg = request.POST.get('percentagepg')
        coursegra = request.POST.get('coursegra')
        schoolcolgra = request.POST.get('schoolcolgra')
        yearofpassingra = request.POST.get('yearofpassingra')
        percentagegra = request.POST.get('percentagegra')
        coursessc = request.POST.get('coursessc')
        schoolcolssc = request.POST.get('schoolcolssc')
        yearofpassingssc = request.POST.get('yearofpassingssc')
        percentagessc = request.POST.get('percentagessc')
        coursehsc = request.POST.get('coursehsc')
        schoolcolghsc = request.POST.get('schoolcolghsc')
        yearofpassinghsc = request.POST.get('yearofpassinghsc')
        percentagehsc = request.POST.get('percentagehsc')

        try:
            education.coursepg = coursepg
            education.schoolcolgpg = schoolcolgpg
            education.yearofpassingpg = yearofpassingpg
            education.percentagepg = percentagepg
            education.coursegra = coursegra
            education.schoolcolgra = schoolcolgra
            education.yearofpassingra = yearofpassingra
            education.percentagegra = percentagegra
            education.coursessc = coursessc
            education.schoolcolssc = schoolcolssc
            education.yearofpassingssc = yearofpassingssc
            education.percentagessc = percentagessc
            education.coursehsc = coursehsc
            education.schoolcolghsc = schoolcolghsc
            education.yearofpassinghsc = yearofpassinghsc
            education.percentagehsc = percentagehsc
            education.save()

            error = "no"
        except Exception as e:
            error = "yes"
            print(f"Exception: {e}")

    context = {'error': error, 'education': education}
    return render(request, 'edit_myeducation.html', context)

@login_required(login_url='emp_login')
def change_password(request):
    error = ""
    user = request.user

    if request.method == 'POST':
        c = request.POST['currentpassword']
        n = request.POST['npassword']

        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"
        except Exception as e:
            error = "yes"
            print(f"Exception: {e}")

    context = {'error': error}
    return render(request, 'change_password.html', context)

@login_required(login_url='emp_login')
def user_logout(request):
    logout(request)
    return redirect('index')

def admin_login(request):
    return render(request, 'admin_login.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('admin_home')
            else:
                messages.error(request, 'You do not have admin privileges.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'admin_login.html')

def admin_home(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('admin_login')
    return render(request, 'admin_home.html')