from django.db import models
from django.contrib.auth.models import User
class EmployeeDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    empcode = models.CharField(max_length=50)
    empdept = models.CharField(max_length=20,null=True)
    designatation = models.CharField(max_length=100)