from django.contrib import admin
from django.urls import path
from program_and_curriculum_management import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('programme',views.programme, name='program_and_curriculum_management'),
    path('curriculum/<pro_id>',views.curriculum, name='curriculum'),
    path('courses',views.courses, name='courses'),
    path('semester/<curr_id>',views.semester, name='semester'),
    path('add_programme',views.add_programme, name='add_programme') 
]
