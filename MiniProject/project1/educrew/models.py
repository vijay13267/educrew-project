from django.db import models

# Create your models here.

class Dept(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=60)
    def __str__(self):
        return self.dept_name

class Student(models.Model):
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
    
    def __str__(self):
        return self.firstname +" "+  self.lastname

class Lecturer(models.Model):
    lect_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100)
    phoneno = models.IntegerField(null=True)

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
    dept_id = models.ForeignKey(Dept, null=True, on_delete=models.CASCADE)
    sec = models.IntegerField(null=True)
    def __str__(self):
        return str(self.sub_id)

class StudentSchedule(models.Model):
    dept_id = models.ForeignKey(Dept, null=True, on_delete=models.SET_NULL)
    sec = models.IntegerField(null=True)
    WEEK = (('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),('Thursday','Thursday'),('Friday','Friday'),('Saturday','Saturday'),('Sunday','Sunday'))
    day = models.CharField(choices=WEEK, max_length=10, null=True)

    p1 = models.IntegerField(null=True, blank=True)
    p2 = models.IntegerField(null=True, blank=True)
    p3 = models.IntegerField(null=True, blank=True)
    p4 = models.IntegerField(null=True, blank=True)


class LecturerSchedule(models.Model):
    lect_id = models.ForeignKey(Lecturer, null=True, on_delete=models.SET_NULL) 
    WEEK = (('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),('Thursday','Thursday'),('Friday','Friday'),('Saturday','Saturday'),('Sunday','Sunday'))
    day = models.CharField(choices=WEEK, max_length=10, null=True)

    p1 = models.IntegerField(null=True, blank=True)
    p2 = models.IntegerField(null=True, blank=True)
    p3 = models.IntegerField(null=True, blank=True)
    p4 = models.IntegerField(null=True, blank=True)


