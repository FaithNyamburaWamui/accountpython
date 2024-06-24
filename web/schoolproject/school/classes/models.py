from django.db import models

# Create your models here.

class Classes(models.Model):
    student_id=models.SmallIntegerField()
    class_rules=models.TextField()
    class_capacity=models.SmallIntegerField()
    class_perfomance=models.IntegerField()
    class_lecture=models.CharField(max_length=20)
    class_id=models.IntegerField()
    class_representative=models.CharField(max_length=20)
    class_name=models.CharField()
    class_description=models.TextField()
    class_table_number=models.SmallIntegerField()
    class_bio=models.CharField(max_length=20)

def __str__(self):
    return f'{self.class_capacity} {self.class_id}'