from django.db import models

class Student(models.Model):
    student_id=models.SmallIntegerField()
    first_name=models.CharField(max_length=20)
    last_name=models.CharField()
    code=models.SmallIntegerField()
    email=models.EmailField()
    age=models.SmallIntegerField()
    country=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)
    next_of_kin=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    bio=models.TextField()
    picture=models.ImageField()


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
