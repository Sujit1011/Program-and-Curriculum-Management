from django.db import models
from datetime import date

# Create your models here.
class Programme(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100) 
    def __str__(self):
        return self.title
    
    

class Curriculum(models.Model):
    name = models.CharField(max_length=100)
    batch_year = models.IntegerField(default=date.today().year)
    version = models.IntegerField(default=0)
    programme_id = models.ForeignKey(Programme, on_delete=models.CASCADE)

class Semester(models.Model):
    semester_no = models.IntegerField()
    curriculum_id = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    # course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)


class Courses(models.Model):
    course_code = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    credits = models.IntegerField(default=0)
    contact_hours_Lecture = models.IntegerField(default=0)
    contact_hours_Tutorial = models.IntegerField(default=0)
    contact_hours_Lab = models.IntegerField(default=0)
    syllabus = models.CharField(max_length=5000)
    evaluation_schema = models.CharField(max_length=1000)
    ref_books = models.CharField(max_length=2000)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
