from django.db import models

class DemoDb(models.Model):
    CategoryName = models.CharField(max_length=50, null=True, blank=True)
    Description = models.TextField(max_length=50, null=True, blank=True)
    CategoryImage = models.ImageField(upload_to="Category_Pictures", null=True, blank=True)

# Create your models here.
