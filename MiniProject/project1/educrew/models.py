from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Dept(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=60)
    dept_short = models.CharField(max_length=10,blank=True)
    def __str__(self):
        return self.dept_name

class Student(models.Model):
    user = models.OneToOneField(User,null=True, blank=True ,on_delete=models.CASCADE)
    rollno = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100)
    phoneno = models.IntegerField(null=True)

    YEAR = ((1,1),(2,2),(3,3),(4,4))
    SEC=((1,1),(2,2),(3,3))

    year = models.IntegerField(choices=YEAR, null=True)
    dept_id = models.ForeignKey(Dept, null=True, on_delete=models.SET_NULL) #cascade
    sec = models.IntegerField(choices=SEC, null=True)
    profile_image= models.ImageField(default="profilepic.jpg",null=True)
    def __str__(self):
        return self.firstname +" "+  self.lastname

class Lecturer(models.Model):
    user = models.OneToOneField(User,null=True, blank=True ,on_delete=models.CASCADE)
    lect_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100)
    phoneno = models.IntegerField(null=True)
    cabin_no = models.CharField(max_length=50, null=True, blank=True)
    profile_image= models.ImageField(default="profilepic.jpg",null=True)


    dept_id = models.ForeignKey(Dept, null=True, on_delete=models.SET_NULL) #cascade
    
    def __str__(self):
        return self.firstname +" "+  self.lastname


class Subject(models.Model):
    sub_id = models.IntegerField(primary_key=True)
    sub_name = models.CharField(max_length=50)
    def __str__(self):
        return self.sub_name


class SubjectInfo(models.Model):
    unq_id = models.IntegerField(primary_key=True)
    lect_id = models.ForeignKey(Lecturer, null=True, on_delete=models.CASCADE)
    sub_id = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    year = models.IntegerField(null=True)
    dept_id = models.ForeignKey(Dept, null=True, on_delete=models.CASCADE)
    sec = models.IntegerField(null=True)
    def __str__(self):
        return str(self.unq_id)+": "+str(self.sub_id)+" "+str(self.dept_id)+" " +str(self.sec)+" sec"

class StudentSchedule(models.Model):
    dept_id = models.ForeignKey(Dept, null=True, on_delete=models.SET_NULL)
    year = models.IntegerField(null=True)
    sec = models.IntegerField(null=True)
    WEEK = (('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),('Thursday','Thursday'),('Friday','Friday'),('Saturday','Saturday'),('Sunday','Sunday'))
    day = models.CharField(choices=WEEK, max_length=10, null=True)

    p1 = models.IntegerField(null=True, blank=True)
    p2 = models.IntegerField(null=True, blank=True)
    p3 = models.IntegerField(null=True, blank=True)
    p4 = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.year)+" yr "+str(self.dept_id)+" dept "+str(self.sec)+" sec "+self.day

class LecturerSchedule(models.Model):
    lect_id = models.ForeignKey(Lecturer, null=True, on_delete=models.SET_NULL) 
    WEEK = (('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),('Thursday','Thursday'),('Friday','Friday'),('Saturday','Saturday'),('Sunday','Sunday'))
    day = models.CharField(choices=WEEK, max_length=10, null=True)

    p1 = models.IntegerField(null=True, blank=True)
    p2 = models.IntegerField(null=True, blank=True)
    p3 = models.IntegerField(null=True, blank=True)
    p4 = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.lect_id)+" "+self.day+"'s schedule"

class Announcements(models.Model):
    lect_id = models.ForeignKey(Lecturer, null=True, on_delete=models.SET_NULL) 
    year = models.IntegerField(null=True)
    dept_id = models.ForeignKey(Dept, null=True, on_delete=models.SET_NULL)
    sec = models.IntegerField(null=True)
    start_date = models.DateField(null=True,default=date.today)
    end_date = models.DateField(null=True,default=date.today)  
    note = models.CharField(null=True, max_length=500)

    def __str__(self): 
        return self.note


class StudentAchievement(models.Model):
    rollno = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    lang_known = models.CharField(null=True,blank=True, max_length=500)
    prog_lang = models.CharField(null=True,blank=True, max_length=500)
    internships = models.CharField(null=True,blank=True, max_length=500)
    projects = models.CharField(null=True,blank=True, max_length=500)
    links = models.CharField(null=True,blank=True, max_length=500)
    sports = models.CharField(null=True,blank=True, max_length=500)
    other = models.CharField(null=True,blank=True, max_length=500)

    def __str__(self):
        return str(self.rollno)+"'s Achievements"

class FacultyAchievement(models.Model):
    lect_id = models.ForeignKey(Lecturer, null=True, on_delete=models.SET_NULL)
    lang_known = models.CharField(null=True,blank=True, max_length=500)
    qual = models.CharField(null=True,blank=True, max_length=500)
    spcltns = models.CharField(null=True,blank=True, max_length=500)
    projects = models.CharField(null=True,blank=True, max_length=500)
    research = models.CharField(null=True,blank=True, max_length=500)
    other = models.CharField(null=True,blank=True, max_length=500)
    def __str__(self):
        return str(self.lect_id)+"'s Achievements"