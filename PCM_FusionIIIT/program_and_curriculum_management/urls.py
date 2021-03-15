from django.contrib import admin
from django.urls import path
from program_and_curriculum_management import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('programme',views.programme, name='program_and_curriculum_management'),
    path('courses',views.courses, name='courses'),
    path('semester',views.semester, name='semester'),
]