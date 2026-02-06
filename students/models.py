from django.db import models

# Create your models here.
class Student(models.Model):
    sems=[(1,'1st sem'),(2,'2nd sem'),(3,'3rd sem'),(4,'4th sem')]
    slno=models.IntegerField(unique=True)
    name=models.CharField(max_length=45)
    sem=models.IntegerField(choices=sems)
    course=models.CharField(max_length=20)

    def __str__(self):#str(), __int__, __add__
        return self.name

#Student table with 4 columns of specified name and type will be created
    