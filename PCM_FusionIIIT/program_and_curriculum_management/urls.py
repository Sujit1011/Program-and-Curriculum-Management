from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from program_and_curriculum_management import views

app_name = 'program_and_curriculum_management'

urlpatterns = [
    #path('admin/', admin.site.urls)
    url(r'^$', views.program_and_curriculum_management, name='program_and_curriculum_management'),
    url(r'^programme/$', views.programme, name='programme'),
    url(r'^curriculum/(?P<pro_id>[0-9]+)$', views.curriculum, name='curriculum'),
    url(r'^courses/(?P<cour_id>[0-9]+)$', views.courses, name='courses'),
    url(r'^semester/(?P<cur_id>[0-9]+)$', views.semester, name='semester'),
    url(r'^add_programme/$', views.add_programme, name='add_programme'),
    url(r'^add_course/$', views.add_course, name='add_course'),
    url(r'^add_curriculum_semester/$', views.add_curriculum_semester, name='add_curriculum_semester'),
    url(r'^add_course_curriculum/$', views.add_course_curriculum, name='add_course_curriculum'),
    url(r'^update_course/(?P<cour_id>[0-9]+)$', views.update_course, name='update_course')


    # path('programme',views.programme, name='program'),
    # path('curriculum/<pro_id>',views.curriculum, name='curriculum'),
    # path('courses/<cour_id>',views.courses, name='courses'),
    # path('semester/<cur_id>',views.semester, name='semester'),
    # path('add_programme',views.add_programme, name='add_programme'),
    # path('add_course',views.add_course, name='add_course'),
    # path('add_curriculum_semester',views.add_curriculum_semester, name='add_curriculum_semester'),
    # path('add_course_curriculum',views.add_course_curriculum, name='add_course_curriculum'),
    # path('update_course/<cour_id>',views.update_course, name='update_course')   
]
