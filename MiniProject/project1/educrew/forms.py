from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import *

class AnnounceForm(ModelForm):
    # date = forms.DateField(label='Date(YYYY-MM-DD)',initial=datetime.date.today)
    note = forms.CharField(label='Note to Announce')
    class Meta:
        model = Announcements
        fields= '__all__'
        exclude = ['lect_id']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
        ]

class ProfileForm(forms.ModelForm):
    phoneno = forms.IntegerField(label='Phone Number')
    class Meta:
        model = Student
        fields = ['email','phoneno','profile_image']
        
class ProfileForm2(forms.ModelForm):
    phoneno = forms.IntegerField(label='Phone Number')
    class Meta:
        model = Lecturer
        fields = ['email','phoneno','cabin_no','profile_image']

class StuAchvmntsForm(forms.ModelForm):
    lang_known = forms.CharField(label='Languages Known')
    prog_lang = forms.CharField(label='Programming Languages')
    internships = forms.CharField(label='Internships')
    projects = forms.CharField(label='Projects')
    sports = forms.CharField(label='Links (if any)')
    other = forms.CharField(label='Sports')
    
    class Meta:
        model = StudentAchievement
        fields = '__all__'
        exclude = ['rollno']

class FacAchvmntsForm(forms.ModelForm):
    lang_known = forms.CharField(label='Languages Known')
    qual = forms.CharField(label='Education Qualifications')
    spcltns = forms.CharField(label='Specializations')
    projects = forms.CharField(label='Projects')
    research = forms.CharField(label='Research Works')
    other = forms.CharField(label='Other Achievements')
    class Meta:
        model = FacultyAchievement
        fields = '__all__'
        exclude = ['lect_id']
