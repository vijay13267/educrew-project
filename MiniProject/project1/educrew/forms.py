from django.forms import ModelForm
from django import forms
from .models import Announcements

class AnnounceForm(ModelForm):
    class Meta:
        model = Announcements
        fields= '__all__'
        exclude = ['lect_id']