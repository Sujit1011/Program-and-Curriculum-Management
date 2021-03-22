from django.db import models
from datetime import date

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
    programme_id = models.ForeignKey(Programme, on_delete=models.CASCADE)
    def __str__(self):
        return self.name +" "+ self.version


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
        return self.course_code +" - "+ self.title
    # semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)


class Semester(models.Model):
    semester_no = models.IntegerField()
    curriculum_id = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.semester_no)



