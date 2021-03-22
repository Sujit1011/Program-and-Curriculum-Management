from django.shortcuts import render, HttpResponse
from .models import Programme, Curriculum, Semester

# Create your views here.


def programme(request):
    ug = Programme.objects.filter(category='UG')
    pg = Programme.objects.filter(category='PG')
    phd = Programme.objects.filter(category='PHD') 
    return render(request,'programme.html',{'UG':ug, 'PG':pg, 'PHD':phd})

def curriculum(request, pro_id):
    current_curriculum = Curriculum.objects.filter(present_curriculum=1).filter(programme_id_id=pro_id)
    past_curriculum = Curriculum.objects.filter(present_curriculum=0).filter(programme_id_id=pro_id)
    title = Programme.objects.filter(id=pro_id)[0]
    return render(request,'curriculum.html',{'Current_curriculum': current_curriculum, 'Past_curriculum': past_curriculum, 'Title':title})

def semester(request, curr_id):
    curr_name = Curriculum.objects.filter(id=curr_id)[0]
    return render(request,'semester.html',{'Curr_name':curr_name})

def courses(request):
    return render(request,'courses.html')


def add_programme(request):
    return render(request,'add_programme.html')