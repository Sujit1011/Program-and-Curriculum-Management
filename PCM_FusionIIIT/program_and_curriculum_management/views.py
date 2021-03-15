from django.shortcuts import render, HttpResponse

# Create your views here.


def programme(request):
    return render(request,'programme.html')

def courses(request):
    return render(request,'courses.html')

def semester(request):
    return render(request,'semester.html')