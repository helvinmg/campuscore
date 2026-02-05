from django.db import models

# Create your models here.
class Student(models.Model):
    slno=models.IntegerField(unique=True)
    name=models.CharField(max_length=40)
    sem=models.IntegerField()
    course=models.CharField(max_length=20)

#Student table with 4 columns of specified name and type will be created
    