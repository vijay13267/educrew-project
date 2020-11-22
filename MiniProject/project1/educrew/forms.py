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
    phoneno = forms.IntegerField(label='Phone Number',required=False)
    class Meta:
        model = Student
        fields = ['email','phoneno','profile_image']
        
class ProfileForm2(forms.ModelForm):
    phoneno = forms.IntegerField(label='Phone Number',required=False)
    class Meta:
        model = Lecturer
        fields = ['email','phoneno','cabin_no','profile_image']

class StuAchvmntsForm(forms.ModelForm):
    lang_known = forms.CharField(label='Languages Known',required=False)
    prog_lang = forms.CharField(label='Programming Languages',required=False)
    internships = forms.CharField(label='Internships',required=False)
    projects = forms.CharField(label='Projects',required=False)
    links = forms.CharField(label='Links (if any)',required=False)
    sports = forms.CharField(label='Sports',required=False)
    other = forms.CharField(label='Other Achievements',required=False)
    
    class Meta:
        model = StudentAchievement
        fields = '__all__'
        exclude = ['rollno']

class FacAchvmntsForm(forms.ModelForm):
    lang_known = forms.CharField(label='Languages Known',required=False)
    qual = forms.CharField(label='Education Qualifications',required=False)
    spcltns = forms.CharField(label='Specializations',required=False)
    projects = forms.CharField(label='Projects',required=False)
    research = forms.CharField(label='Research Works',required=False)
    other = forms.CharField(label='Other Achievements',required=False)
    class Meta:
        model = FacultyAchievement
        fields = '__all__'
        exclude = ['lect_id']
