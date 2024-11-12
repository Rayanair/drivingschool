from django.contrib import admin
from .models import Student, Instructor, Secretary, Appointment, StudentPackage

admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Secretary)
admin.site.register(Appointment)
admin.site.register(StudentPackage)
