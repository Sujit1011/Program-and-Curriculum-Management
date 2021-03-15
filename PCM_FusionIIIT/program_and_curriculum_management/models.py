from django.db import models

# Create your models here.
class courses_list(models.Model):
    Course_code = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Credits = models.IntegerField(default=0)
    Syllabus = models.CharField(max_length=1000)
    Evaluation_schema = models.CharField(max_length=100)
    Ref_books = models.CharField(max_length=1000)
