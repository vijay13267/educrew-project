import django_filters
from django_filters import CharFilter,DateFilter
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

class SearchFilter(django_filters.FilterSet):
    firstname = CharFilter(label='First Name', field_name='firstname',lookup_expr='icontains')
    class Meta:
        model = Lecturer
        fields = ['firstname']

class AnnFilter(django_filters.FilterSet):
    strt_date = DateFilter(lookup_expr='gte')
    end_date = DateFilter(lookup_expr='lte')
    class Meta:
        model = Announcements
        fields = ['strt_date','end_date']