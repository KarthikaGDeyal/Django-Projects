from django.db import models

# Create your models here.
class StudentDb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Address = models.TextField(max_length=50, null=True, blank=True)
    Course = models.CharField(max_length=50, null=True, blank=True)
    Gender = models.CharField(max_length=50, null=True, blank=True)

class BookDb(models.Model):
    BookName = models.CharField(max_length=50, null=True, blank=True)
    AuthorName = models.CharField(max_length=50, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    PublishedDate = models.DateField(null=True, blank=True)

