from django.shortcuts import render, HttpResponse
from .models import Programme

# Create your views here.


def programme(request):
    ug = Programme.objects.filter(category='UG')
    pg = Programme.objects.filter(category='PG')
    phd = Programme.objects.filter(category='PHD') 
    return render(request,'programme.html',{'UG':ug, 'PG':pg, 'PHD':phd})

def curriculum(request):
    return render(request,'curriculum.html')

def courses(request):
    return render(request,'courses.html')

def semester(request):
    return render(request,'semester.html')