from django.contrib import admin
from django.urls import path
from employee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('registration',registration,name='registration'),
]
