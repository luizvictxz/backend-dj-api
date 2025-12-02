from django.contrib import admin

from .models import Course, Registration, Student

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Registration)
