from django.db import models

# Create your models here.
class StudentDb(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    Place=models.CharField(max_length=50,null=True,blank=True)
    Course = models.CharField(max_length=50, null=True, blank=True)
    Age=models.IntegerField(null=True,blank=True)
    Mobile_Number = models.IntegerField(null=True, blank=True)


class Demo_table(models.Model):
    Emp_Name=models.CharField(max_length=50,null=True,blank=True)
    Company=models.CharField(max_length=50,null=True,blank=True)
    Mobile_Number=models.IntegerField(null=True,blank=True)
    Salary = models.IntegerField(null=True, blank=True)


