from django.forms import ModelForm
from .models import Programme, Curriculum, Courses, CourseSlot, Semester

class ProgrammeForm(ModelForm):  
    class Meta:
        model = Programme
        fields = '__all__'

class CurriculumForm(ModelForm):  
    class Meta:
        model = Curriculum
        fields = '__all__'

class CoursesForm(ModelForm):   
    class Meta:
        model = Courses
        # fields = ("course_code",
        # "title","contact_hours_Lecture",
        # "contact_hours_Tutorial",
        # "contact_hours_Lab",
        # "contact_hours_Discussion",
        # "contact_hours_Project",
        # "syllabus",
        # "evaluation_schema_quiz1",
        # "evaluation_schema_midsem",
        # "evaluation_schema_quiz2",
        # "evaluation_schema_lab",
        # "evaluation_schema_endsem",
        # "ref_books")
        fields = "__all__"
        # exclude = ("credits",)

class SemesterForm(ModelForm):
    class Meta:
        model = Semester
        fields = ("semester_no","curriculum_id")

class SemesterCourseForm(ModelForm):
    
    class Meta:
        model = CourseSlot
        fields = ("course_id",)


class CourseForm(ModelForm):   
    class Meta:
        model = Courses
        fields = ("credits",)
