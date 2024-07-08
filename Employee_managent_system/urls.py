from django.contrib import admin
from django.urls import path
from employee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('registration/', registration, name='registration'),
    path('emp_login/', emp_login, name='emp_login'),
    path('emp_home/', emp_home, name='emp_home'),
    path('profile/', profile, name='profile'),
    path('logout/', user_logout, name='user_logout'),
    
    path('admin_login/', admin_login, name='admin_login'),
    path('admin_home/', admin_home, name='admin_home'),
    
    path('my_experience/', my_experience, name='my_experience'),
    path('edit_my_experience/', edit_my_experience, name='edit_my_experience'),
    path('my_education/', my_education, name='my_education'),
    path('edit_myeducation/', edit_myeducation, name='edit_myeducation'),
    path('change_password/', change_password, name='change_password'),
    path('change_password_admin/', change_password_admin, name='change_password_admin'),
    path('all_employee/', all_employee, name='all_employee'),
    path('edit_employee/<int:pid>/', edit_employee, name='edit_employee'),
    path('delete_employee/<int:pid>/', delete_employee, name='delete_employee'),
    path('edit_education/<int:pid>/', edit_education, name='edit_education'),
]
