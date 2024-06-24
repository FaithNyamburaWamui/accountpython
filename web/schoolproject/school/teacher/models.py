from django.db import models

# Create your models here.

class Teacher(models.Model):
    teacher_age=models.SmallIntegerField()
    teacher_name=models.CharField(max_length=20)
    teacher_id=models.SmallIntegerField()
    teacher_course=models.CharField(max_length=20)
    teacher_contact=models.CharField(max_length=20)
    teacher_description=models.TextField(max_length=20)
    teacher_occupation=models.CharField(max_length=20)
    teacher_salary=models.SmallIntegerField()
    teacher_headshot=models.ImageField()
    teacher_bank_account=models.IntegerField()
    student_id=models.SmallIntegerField()

    def __str__(self):
        return f'{self.teacher_description} {teacher_age}'
