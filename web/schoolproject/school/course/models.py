from django.db import models

# Create your models here.

class Courses(models.Model):
    courses_name=models.CharField(max_length=20)
    courses_code=models.IntegerField()
    courses_TA=models.CharField(max_length=20)
    courses_term=models.CharField(max_length=20)
    courses_description=models.TextField()
    courses_department=models.CharField(max_length=20)
    courses_syllabus=models.CharField(max_length=20)
    courses_instructor=models.CharField(max_length=20)
    courses_duration=models.SmallIntegerField()
    student_id=models.SmallIntegerField()


def __str__(self):
    return f'{self.courses_assignment} {self.courses_department}'
