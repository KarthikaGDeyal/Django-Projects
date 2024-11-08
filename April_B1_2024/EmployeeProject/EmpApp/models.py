from django.db import models

class EmployeeDb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Salary = models.IntegerField(null=True, blank=True)
    Location = models.CharField(max_length=50, null=True, blank=True)

class Registration_Db(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Place = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    ProfileImage= models.ImageField(upload_to="Profile_Pictures",null=True,blank=True)


# Create your models here.
