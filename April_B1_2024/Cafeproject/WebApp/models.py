from django.db import models


class ContactDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)

class ContactInfoDb(models.Model):
    Place = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Description1 = models.CharField(max_length=100, null=True, blank=True)
    Description2 = models.CharField(max_length=100, null=True, blank=True)
    Description3 = models.CharField(max_length=100, null=True, blank=True)



class RegisterDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    ConfirmPassword = models.CharField(max_length=100, null=True, blank=True)

class ClassRegistrationDb(models.Model):
    CLASS_CHOICES = [
        ('Online', 'OnlineClass'),
        ('Offline', 'OfflineClass'),
    ]

    Name = models.CharField(max_length=100, null=True, blank=True)
    Phone=models.IntegerField(null=True, blank=True)
    StudyingClass=models.CharField(max_length=100,choices=CLASS_CHOICES, null=True, blank=True)
    Requirements=models.CharField(max_length=100, null=True, blank=True)


class TeamDb(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    POSITION_CHOICES = [
        ('PastryChef', 'PastryChef'),
        ('Decorator', 'Decorator'),
        ('Assistant', 'Assistant'),
        ('Recipe Developer', 'Recipe Developer'),
        ('Kitchen Porter', 'Kitchen Porter'),
        ('Head Baker', 'Head Baker'),
    ]
    ProfileImage = models.ImageField(upload_to='profile/', null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Gender = models.CharField(max_length=100,choices=GENDER_CHOICES, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Position = models.CharField(max_length=100, choices=POSITION_CHOICES,null=True, blank=True)
    Resume=models.FileField(upload_to='resumes/', null=True, blank=True)


class TestimonialDb(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    ProfileImage = models.ImageField(upload_to='profile/', null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Review = models.CharField(max_length=100, null=True, blank=True)
    Rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1)

class CartDb(models.Model):
        Username = models.CharField(max_length=100, null=True, blank=True)
        Product_name = models.CharField(max_length=100, null=True, blank=True)
        Quantity = models.IntegerField(null=True, blank=True)
        discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
        Price = models.IntegerField(null=True, blank=True)
        Total_price = models.FloatField(null=True, blank=True)

class OrderDb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Town_City = models.CharField(max_length=100, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    PostCode_ZIP = models.IntegerField(null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Total_price = models.FloatField(null=True, blank=True)
    Order_notes = models.CharField(max_length=100, null=True, blank=True)
    payment_status = models.CharField(max_length=20, default='Pending')

class WishlistDb(models.Model):
    STOCK_STATUS = [
        ('in_stock', 'In Stock'),
        ('out_of_stock', 'Out of Stock'),
    ]
    Username = models.CharField(max_length=100, null=True, blank=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Stock=models.CharField(max_length=100,choices=STOCK_STATUS,null=True, blank=True)

class FooterDb(models.Model):
    Description1= models.CharField(max_length=100, null=True, blank=True)
    Description2 = models.CharField(max_length=100, null=True, blank=True)
    Description3 = models.CharField(max_length=100, null=True, blank=True)
    Description4 = models.CharField(max_length=100, null=True, blank=True)
    Description5 = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)

class AboutDb(models.Model):
    Description = models.TextField(max_length=900, null=True, blank=True)
    Description1 = models.TextField(max_length=900, null=True, blank=True)




