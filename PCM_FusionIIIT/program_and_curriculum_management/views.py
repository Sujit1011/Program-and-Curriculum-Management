from django.shortcuts import render, HttpResponse

# Create your views here.


def programme(request):
    return render(request,'programme.html')