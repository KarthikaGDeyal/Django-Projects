from django.db import models
class Registration_Db(models.Model):
    ShopName = models.CharField(max_length=50, null=True, blank=True)
    Place = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    OwnerName=models.CharField(max_length=50, null=True, blank=True)
    ShopType=models.CharField(max_length=50, null=True, blank=True)
    ProfileImage= models.ImageField(upload_to="Profile_Pictures",null=True,blank=True)

# Create your models here.
