from django.db import models

# Create your models here.
class StudentRegistration(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    Place = models.CharField(max_length=50, null=True, blank=True)
    Course = models.CharField(max_length=50, null=True, blank=True)
    Company = models.CharField(max_length=50, null=True, blank=True)
    Salary = models.IntegerField(null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Address = models.TextField(max_length=50, null=True, blank=True)
    Designation = models.CharField(max_length=50, null=True, blank=True)
    Gender=models.CharField(max_length=50, null=True, blank=True)
