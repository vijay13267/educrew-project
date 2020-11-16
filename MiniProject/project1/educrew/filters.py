import django_filters

from .models import *

class LecturerFilter(django_filters.FilterSet):
    class Meta:
        model = Lecturer
        fields = '__all__'
        exclude = ['email','phoneno']

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['email','phoneno']