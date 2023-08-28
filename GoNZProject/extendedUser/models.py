from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class NewUser(AbstractUser):
    Position_Choice=[
        ('System Administrator','System Administrator'),
        ('Technical Director','Technical Director'),
        ('Senior Agent','Senior Agent'),
        ('Agent','Agent'),
        ('Managing Director','Managing Director'),
        ('Area Manager','Area Manager'),
    ]
    Department_Choice=[
        ('Administrator','Administrator'),
        ('Agent','Agent'),
        ('Management','Management'),
      
    ]
    position=models.CharField(max_length=100,choices=Position_Choice,null=True,blank=True)
    department=models.CharField(max_length=100,choices=Department_Choice,null=True,blank=True)
    
    user_image = models.ImageField(upload_to='user_images/', null=True, blank=True)