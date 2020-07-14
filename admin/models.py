from django.db import models
import datetime
class AdminTable(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True,error_messages={"unique":"Email ID is Already Exists",})
    password=models.CharField(max_length=150)
    contact_no=models.IntegerField(unique=True,error_messages={"unique":"Phone Number is Already Exists",})
    creation_date=models.DateTimeField(auto_now=True)

class CourseTable(models.Model):
    course_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,unique=True,error_messages={"unique":"Course is Already Exists"})
    fee=models.FloatField()

    def __str__(self):
        return self.name

class ScheduleclassesTable(models.Model):
    class_id=models.AutoField(primary_key=True)
    course=models.ForeignKey(CourseTable,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    duration=models.IntegerField()