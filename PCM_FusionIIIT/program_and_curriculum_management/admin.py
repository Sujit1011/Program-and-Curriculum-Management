from django.contrib import admin
from .models import Programme,Curriculum,Semester,Courses
 
# Register your models here.
admin.site.register(Programme)
admin.site.register(Curriculum)
admin.site.register(Semester)
admin.site.register(Courses)