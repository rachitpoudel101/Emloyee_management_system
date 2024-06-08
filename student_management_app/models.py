from django.db import models

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    Subject_name = models.CharField(max_length=200)
    course_name = models.ForeignKey(Course,on_delete=models.CASCADE)
    
    
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    profile_pic = models.FileField()
    address = models.CharField(max_length=100)