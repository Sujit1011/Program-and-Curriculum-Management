from django.contrib import admin
from .models import Programme,Curriculum,Semester,Courses,Semester_Course_List
 
# Register your models here.
admin.site.register(Programme)
admin.site.register(Curriculum)
admin.site.register(Semester)
admin.site.register(Courses)
admin.site.register(Semester_Course_List)