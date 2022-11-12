from django.contrib import admin


from .models import User, Course, Profile




class CourseAdmin(admin.ModelAdmin):
    model = Course

class ProfileAdmin(admin.ModelAdmin):
    model = Profile

admin.site.register(Course, CourseAdmin)

admin.site.register(Profile, ProfileAdmin)
