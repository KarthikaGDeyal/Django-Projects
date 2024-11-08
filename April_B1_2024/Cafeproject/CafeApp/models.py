from django.db import models
class DemoDb(models.Model):
    CategoryName = models.CharField(max_length=50, null=True, blank=True)
    Description = models.TextField(max_length=50, null=True, blank=True)
    CategoryImage = models.ImageField(upload_to="Category_Pictures", null=True, blank=True)




class ProDb(models.Model):
    CategoryName = models.CharField(max_length=50, null=True, blank=True)
    ProductName = models.CharField(max_length=50, null=True, blank=True)
    Description = models.TextField(max_length=50, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    ProductImage = models.ImageField(upload_to="Product_Pictures", null=True, blank=True)
    ProductImage1 = models.ImageField(upload_to="Product_Pictures", null=True, blank=True)
    ProductImage2 = models.ImageField(upload_to="Product_Pictures", null=True, blank=True)
    ProductImage3 = models.ImageField(upload_to="Product_Pictures", null=True, blank=True)
    ProductImage4 = models.ImageField(upload_to="Product_Pictures", null=True, blank=True)

class ClasslistDb(models.Model):
    ClassName = models.CharField(max_length=50, null=True, blank=True)
    Date = models.CharField(max_length=50, null=True, blank=True)
    Description = models.TextField(max_length=50, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    ClassImage = models.ImageField(upload_to="Class_Pictures", null=True, blank=True)

