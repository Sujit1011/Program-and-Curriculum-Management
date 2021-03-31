from django.shortcuts import render, HttpResponse
from .models import Programme, Curriculum, Semester, Semester_Course_List, Courses
from .forms import ProgrammeForm, CurriculumForm, CoursesForm, SemesterForm, SemesterCourseForm, CourseForm
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

def semester(request, cur_id):
    Curr = Curriculum.objects.filter(id = cur_id).first()
    Sem = Semester.objects.filter(curriculum_id_id = cur_id)
    SCL = Semester_Course_List.objects.all()
    return render(request,'semester.html',{'sem':Sem, 'curr':Curr, 'scl':SCL})

def courses(request,cour_id):
    course_detail = Courses.objects.filter(id = cour_id)
    return render(request,'courses.html',{'Course_detail':course_detail})


# def add_programme(request):
#     if request.method == "POST":
#         Category = request.POST.get('category')
#         Title = request.POST.get('title')
#         programme = Programme(category=Category, title=Title)
#         programme.save()       
#     return render(request,'add_programme.html')

def add_programme(request):
    form = ProgrammeForm()
    if request.method == 'POST':
        form = ProgrammeForm(request.POST)  
        if form.is_valid():
            form.save()
    return render(request,'add_programme.html',{'form':form})

def add_course(request):
    form = CoursesForm()
    if request.method == 'POST':
        form = CoursesForm(request.POST)  
        if form.is_valid():
            form.save()
    return render(request,'add_course.html',{'form':form})
    # if request.method == "POST":
    #     Course_code = request.POST.get('course_code')
    #     Title = request.POST.get('course_name')
    #     Credits = request.POST.get('')
    #     Contact_hours_Lecture = request.POST.get('contact_hour_lecture')
    #     Contact_hours_Tutorial = request.POST.get('contact_hour_tutorial')
    #     Contact_hours_Lab = request.POST.get('contact_hour_lab')
    #     Contact_hours_Discussion = request.POST.get('contact_hour_discussion')
    #     Contact_hours_Project = request.POST.get('contact_hour_project')
    #     Syllabus = request.POST.get('syllabus')
    #     Evaluation_schema_quiz1 = request.POST.get('evaluation_schema_quiz1')
    #     Evaluation_schema_midsem = request.POST.get('evaluation_schema_midsem')
    #     Evaluation_schema_quiz2 = request.POST.get('evaluation_schema_quiz2')
    #     Evaluation_schema_lab = request.POST.get('evaluation_schema_lab')
    #     Evaluation_schema_endsem = request.POST.get('evaluation_schema_endsem')
    #     Ref_books = request.POST.get('reference_books')
    #     courses = Courses(course_code=Course_code, 
    #     title=Title, 
    #     contact_hours_Lecture=Contact_hours_Lecture, 
    #     contact_hours_Tutorial=Contact_hours_Tutorial, 
    #     contact_hours_Lab=Contact_hours_Lab, 
    #     contact_hours_Discussion=Contact_hours_Discussion, 
    #     contact_hours_Project=Contact_hours_Project, 
    #     syllabus=Syllabus, 
    #     evaluation_schema_quiz1=Evaluation_schema_quiz1, 
    #     evaluation_schema_midsem=Evaluation_schema_midsem, 
    #     evaluation_schema_quiz2=Evaluation_schema_quiz2, 
    #     evaluation_schema_lab=Evaluation_schema_lab, 
    #     evaluation_schema_endsem=Evaluation_schema_endsem, 
    #     ref_books=Ref_books)
    #     courses.save()   
    # return render(request,'add_course.html')

def add_curriculum_semester(request):
    form = CurriculumForm()
    if request.method == 'POST':
        form = CurriculumForm(request.POST)  
        if form.is_valid():
            form.save()
    return render(request,'add_curriculum_semster.html',{'form':form})

def add_course_curriculum(request):
    cur = Curriculum.objects.all()
    cour = Courses.objects.all()
    if request.method == "POST":
        curr_id = request.POST.get('currid')
        sem_no = request.POST.get('semno')
        cour_id = request.POST.get('courid')
        semester = Semester(semester_no=sem_no, curriculum_id_id=curr_id)
        semester.save()
        sem = Semester.objects.all().last()
        semester_course = Semester_Course_List(semester_id_id=sem.id, course_id_id=cour_id)
        semester_course.save()
    return render(request,'add_course_curriculum.html',{'cur':cur, 'cour':cour})


def update_course(request,cour_id=0):
    cour = Courses.objects.all()
    cour1 = Courses.objects.get(id=cour_id)
    form = CoursesForm(instance=cour1)
    if request.method == 'POST':
        form = CoursesForm(request.POST, instance=cour1)  
        if form.is_valid():
            form.save()
    return render(request,'update_course.html',{'cour':cour, 'form':form})