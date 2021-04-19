from django.db import models
from datetime import date


# Course Type shuold be editable !!! 

class Constants:
    COURSE_TYPE = (
        ('Professional Core', 'Professional Core'),
        ('Professional Elective', 'Professional Elective'),
        ('Professional Lab', 'Professional Lab'),
        ('Engineering Science', 'Engineering Science'),
        ('Natural Science', 'Natural Science'),
        ('Humanities', 'Humanities'),
        ('Design', 'Design'),
        ('Manufacturing', 'Manufacturing'),
        ('Management Science', 'Management Science'),
    )


# Create your models here.
class Programme(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100) 
    def __str__(self):
        return self.title +" "+ self.category
    
    

class Curriculum(models.Model):
    name = models.CharField(max_length=100)
    batch_year = models.IntegerField(default=date.today().year)
    version = models.CharField(max_length=50)
    present_curriculum = models.BooleanField(default=False)
    no_of_semesters = models.IntegerField(default=8)
    programme_id = models.ForeignKey(Programme, on_delete=models.CASCADE)
    def __str__(self):
        return self.name +" "+ self.version



class DisciplineDepartment(models.Model):
    discipline_name = models.CharField(max_length=50)
    department_head = models.CharField(max_length=50)
    # programme_id = models.ManyToManyField("app.Model", verbose_name=_(""))
    def __str__(self):
        return self.discipline_name +" "+ self.department_head



class ProgrammeDiscipline(models.Model):
    programme_id = models.ForeignKey(Programme, on_delete=models.CASCADE)
    discipline_id = models.ForeignKey(DisciplineDepartment, on_delete=models.CASCADE)


class Batch(models.Model):
    batch_name = models.CharField(max_length=50)
    discipline_id = models.ForeignKey(DisciplineDepartment, on_delete=models.CASCADE)
    curriculum_id = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    def __str__(self):
        return self.batch_name +" "+ str(self.discipline_id) +" "+ str(self.curriculum_id)


class Semester(models.Model):
    semester_no = models.IntegerField()
    curriculum_id = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.semester_no) +" "+ str(self.curriculum_id)


class Courses(models.Model):
    course_code = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    credits = models.IntegerField(default=0)
    contact_hours_Lecture = models.IntegerField(default=0)
    contact_hours_Tutorial = models.IntegerField(default=0)
    contact_hours_Lab = models.IntegerField(default=0)
    contact_hours_Discussion = models.IntegerField(default=0)
    contact_hours_Project = models.IntegerField(default=0)
    syllabus = models.CharField(max_length=5000)
    evaluation_schema_quiz1 = models.IntegerField(default=0)
    evaluation_schema_midsem = models.IntegerField(default=0)
    evaluation_schema_quiz2 = models.IntegerField(default=0)
    evaluation_schema_lab = models.IntegerField(default=0)
    evaluation_schema_endsem = models.IntegerField(default=0)
    ref_books = models.CharField(max_length=2000)
    def __str__(self):
        return self.course_code 
        # +" - "+ self.title
    # semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)


class CourseSlot(models.Model):
    info = models.CharField(max_length=1000, null=True)
    course_type = models.CharField(max_length=40, choices=Constants.COURSE_TYPE, null=True, default='')
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)

#Semester_Course_List