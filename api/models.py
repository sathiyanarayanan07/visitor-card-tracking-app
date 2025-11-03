from django.db import models

# Create your models here.
class user(models.Model):
    username =models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=30,null=True,blank=True)
    phone_number = models.CharField(max_length=30,null=True,blank=True)
    password = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.username
    
class admin_user(models.Model):
    name= models.CharField(max_length=100,null=True,blank=True)
    Organization_name =models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=20,null=True,blank=True)
    password = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.name

