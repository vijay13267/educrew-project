from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Dept)
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Subject)
admin.site.register(SubjectInfo)
admin.site.register(StudentSchedule)
admin.site.register(LecturerSchedule)
admin.site.register(Announcements)


