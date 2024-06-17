from django.db import models

# Create your models here.

class Courses(models.Model):
    courses_name=models.CharField(max_length=20)
    courses_code=models.IntegerField()
    courses_instuctor=models.CharField(max_length=20)
    courses_assignment=models.CharField(max_length=20)
    courses_level=models.CharField(max_length=20)
    courses_department=models.CharField(max_length=20)
    courses_syllabus=models.CharField(max_length=20)
    courses_exams=models.CharField(max_length=20)
    courses_duration=models.IntegerField()


def __str__(self):
    return f'{self.courses_assignment} {self.courses_department}'
