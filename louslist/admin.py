from django.contrib import admin

from .models import User, Course


class CourseAdmin(admin.ModelAdmin):
    model = Course


admin.site.register(Course, CourseAdmin)

