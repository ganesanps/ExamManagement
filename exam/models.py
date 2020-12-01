from django.db import models

# Create your models here.
class Student(models.Model):
    Roll_no=models.CharField(max_length=20)
    Stu_Name=models.CharField(max_length=50)
    DOB=models.DateField()
    Section=models.CharField(max_length=8)
    Mobile=models.CharField(max_length=11)
    Email_ID=models.EmailField(max_length=50)
    Area=models.CharField(max_length=20)
    City=models.CharField(max_length=15)
    State=models.CharField(max_length=20)

    def __str__(self):
        return self.Roll_no
class Faculty(models.Model):
    Faculty_ID=models.CharField(max_length=20)
    Fac_Name=models.CharField(max_length=50)
    Date_of_Joining=models.DateField()
    Position=models.CharField(max_length=20)
    Qualification=models.CharField(max_length=20)

    def __str__(self):
        return self.Faculty_ID
class Course(models.Model):  
    Course_ID=models.CharField(max_length=10)
    Semester=models.IntegerField()
    Course_Name=models.CharField(max_length=30)

    def __str__(self):
        return self.Course_ID
class Schedule(models.Model):
    Course_Name=models.CharField(max_length=30)
    Exam_ID=models.CharField(max_length=20)
    Exam_date=models.DateField()
    Exam_Time=models.TimeField()
    Exam_Type=models.CharField(max_length=20)

    def __str__(self):
        return self.Exam_ID

class Department(models.Model):
    Dept_ID=models.CharField(max_length=20)
    Dept_HOD=models.CharField(max_length=50)
    Dept_Name=models.CharField(max_length=50)

    def __str__(self):
        return self.Dept_ID
class Class(models.Model):
    Class_ID=models.CharField(max_length=20)
    Capacity=models.IntegerField()

    def __str__(self):
        return self.Class_ID
class Grade(models.Model):
    Course_ID=models.CharField(max_length=10)
    Roll_no=models.CharField(max_length=20)
    Grade=models.CharField(max_length=3)

    def __str__(self):
        return self.Roll_no
class Allot(models.Model):
    Exam_ID=models.CharField(max_length=20)
    Roll_no=models.CharField(max_length=20)
    Class_ID=models.CharField(max_length=20)

    def __str__(self):
        return self.Roll_no
class Join(models.Model):
    Roll_no=models.CharField(max_length=20)
    Faculty_ID=models.CharField(max_length=20)
    Course_ID=models.CharField(max_length=10)
    Exam_ID=models.CharField(max_length=20)
    Dept_ID=models.CharField(max_length=20)

    def __list__(self):
        return [self.Roll_no,self.Exam_ID]





