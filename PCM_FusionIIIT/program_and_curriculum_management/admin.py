from django.contrib import admin
from .models import Programme,Curriculum,Semester,Courses,CourseSlot,DisciplineDepartment,ProgrammeDiscipline,Batch
 
# Register your models here.
admin.site.register(Programme)
admin.site.register(Curriculum)
admin.site.register(DisciplineDepartment)
admin.site.register(ProgrammeDiscipline)
admin.site.register(Batch)
admin.site.register(Semester)
admin.site.register(Courses)
admin.site.register(CourseSlot)
