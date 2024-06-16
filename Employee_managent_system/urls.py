from django.contrib import admin
from django.urls import path
from employee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('registration',registration,name='registration'),
    path('emp_login',emp_login,name='emp_login'),
    path('emp_home',emp_home,name='emp_home'),
    path('profile',profile,name='profile'),
    path('logout',logout,name='logout'),
    path('admin_login',admin_login,name='admin_login'),
]
