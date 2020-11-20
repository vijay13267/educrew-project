import django_filters
from django_filters import CharFilter
from .models import *

class LecturerFilter(django_filters.FilterSet):
    firstname = CharFilter(label='First Name', field_name='firstname',lookup_expr='icontains')
    lastname = CharFilter(label='Last Name', field_name='lastname',lookup_expr='icontains')
    class Meta:
        model = Lecturer
        fields = '__all__'
        exclude = ['user','email','phoneno','profile_image','cabin_no']

class StudentFilter(django_filters.FilterSet):
    firstname = CharFilter(label='First Name', field_name='firstname',lookup_expr='icontains')
    lastname = CharFilter(label='Last Name',field_name='lastname',lookup_expr='icontains')
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['user','email','phoneno','profile_image']