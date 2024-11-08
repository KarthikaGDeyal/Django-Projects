from django.db import models

# Create your models here.
class Registration(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Course = models.CharField(max_length=100, null=True, blank=True)
