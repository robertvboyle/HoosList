from django.contrib import admin

from .models import User, Course, Schedule


class CourseAdmin(admin.ModelAdmin):
    model = Course


admin.site.register(Course, CourseAdmin)

admin.site.register(Schedule)
admin.site.register(User)
