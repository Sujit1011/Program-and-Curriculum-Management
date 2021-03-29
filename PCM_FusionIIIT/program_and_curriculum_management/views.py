from django.shortcuts import render, HttpResponse
from .models import Programme, Curriculum, Semester, Semester_Course_List, Courses

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

def semester(request):
    course = Courses.objects.all()
    sem_cr = Semester_Course_List.objects.all()
    sem = Semester.objects.all()
    return render(request,'semester.html')

def courses(request):
    course_detail = Courses.objects.filter(id = 2)
    return render(request,'courses.html',{'Course_detail':course_detail})


def add_programme(request):
    if request.method == "POST":
        Category = request.POST.get('category')
        Title = request.POST.get('title')
        programme = Programme(category=Category, title=Title)
        programme.save()       
    return render(request,'add_programme.html')

def add_course(request):
    if request.method == "POST":
        Course_code = request.POST.get('')
        Title = request.POST.get('')
        Credits = request.POST.get('')
        Contact_hours_Lecture = request.POST.get('')
        Contact_hours_Tutorial = request.POST.get('')
        Contact_hours_Lab = request.POST.get('')
        Contact_hours_Discussion = request.POST.get('')
        Contact_hours_Project = request.POST.get('')
        Syllabus = request.POST.get('')
        Evaluation_schema_quiz1 = request.POST.get('')
        Evaluation_schema_midsem = request.POST.get('')
        Evaluation_schema_quiz2 = request.POST.get('')
        Evaluation_schema_lab = request.POST.get('')
        Evaluation_schema_endsem = request.POST.get('')
        Ref_books = request.POST.get('')
        courses = Courses()
        courses.save()   
    return render(request,'add_course.html')

def add_curriculum_semester(request):
    prog = Programme.objects.all()
    if request.method == 'POST':
        curriculum =  Curriculum()
        curriculum.save()
        return redirect('/')
    return render(request,'add_curriculum_semster.html',{'Prog':prog})

def add_course_curriculum(request):
    cour = Courses.objects.all()
    return render(request,'add_course_curriculum.html',{'Cour':cour})
