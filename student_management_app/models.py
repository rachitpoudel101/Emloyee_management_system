from django.db import models

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
   
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    Subject_name = models.CharField(max_length=200)
    course_name = models.ForeignKey(Course,on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    profile_pic = models.FileField()
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    courde_id = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    objects = models.Manager()
    

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    subject_id = models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    attendence_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
class attendce_report(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendence_id = models.ForeignKey(Attendance,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
class Leave_report_Student(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=100)
    leave_message = models.TextField()
    leave_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Leave_report_Staff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=100)
    leave_message = models.TextField()
    leave_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class FeedBack_Student(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=100)
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Feedback_staff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=100)
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
class notification_staff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
class notification_student(models.Model):
    id = models.AutoField(primary_key=True)
    studemt_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()