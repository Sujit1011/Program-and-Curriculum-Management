from django.contrib import admin
from django.urls import path
from program_and_curriculum_management import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('programme',views.programme, name='program_and_curriculum_management'),
    path('curriculum/<pro_id>',views.curriculum, name='curriculum'),
    path('courses/<cour_id>',views.courses, name='courses'),
    path('semester/<cur_id>',views.semester, name='semester'),
    path('add_programme',views.add_programme, name='add_programme'),
    path('add_course',views.add_course, name='add_course'),
    path('add_curriculum_semester',views.add_curriculum_semester, name='add_curriculum_semester'),
    path('add_course_curriculum',views.add_course_curriculum, name='add_course_curriculum'),
    path('update_course/<cour_id>',views.update_course, name='update_course')   
]
