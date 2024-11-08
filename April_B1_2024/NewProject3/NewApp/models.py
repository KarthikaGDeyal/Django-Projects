from django.db import models

# Create your models here.
class StudentDb(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    Place=models.CharField(max_length=50,null=True,blank=True)
    Age=models.IntegerField(null=True,blank=True)
