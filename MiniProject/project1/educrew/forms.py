from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Announcements,Student,Lecturer

class AnnounceForm(ModelForm):
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
    class Meta:
        model = Student
        fields = ['email','phoneno','profile_image']
        
class ProfileForm2(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['email','phoneno','cabin_no','profile_image']