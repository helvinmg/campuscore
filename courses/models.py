from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=40)
    specialization=models.CharField(max_length=60)
    fee=models.FloatField()
    accreditation=models.BooleanField(default=False)