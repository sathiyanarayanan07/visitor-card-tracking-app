from django.db import models

# Create your models here.
class user(models.Model):
    profile = models.ImageField(upload_to="profile/",null=True,blank=True)
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

class employee_user(models.Model):
    profile = models.ImageField(upload_to="profile/",null=True,blank=True)
    username =models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=30,null=True,blank=True)
    phone_number = models.CharField(max_length=30,null=True,blank=True)
    password = models.CharField(max_length=30,null=True,blank=True)
    role_type = models.CharField(max_length=100,null=True,blank=True,default="employee")


    def __str__(self):
        return self.username


class scan_card(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    company_name=models.CharField(max_length=100,null=True,blank=True)
    email= models.EmailField(max_length=30,null=True,blank=True)
    address =models.TextField(max_length=100,null=True,blank=True)
    Phone_number =models.CharField(max_length=100,null=True,blank=True)
    office_number =models.CharField(max_length=100,null=True,blank=True)
    company_website =models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name
    
class schedule_meeting(models.Model):
    card = models.ForeignKey(scan_card,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    mobile_no =models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    purpose_of_meeting =models.CharField(max_length=100,null=True,blank=True)
    meeting_type =models.CharField(max_length=100,null=True,blank=True,default="Google meet")
    Date = models.DateField(null=True,blank=True)
    Time =models.TimeField(null=True,blank=True)
    meeting_link = models.URLField(null=True,blank=True)
    is_accept = models.BooleanField(null=True,blank=True)
    is_reject = models.BooleanField(null=True,blank=True)
    is_closed =models.BooleanField(null=True,blank=True)

    def __str__(self):
        return f"{self.card.name}--{self.name}--{self.id}"
    


class eventpost(models.Model):
    User = models.ForeignKey(user,on_delete=models.CASCADE,null=True,blank=True)
    caption = models.TextField(null=True,blank=True)
    media =models.FileField(upload_to="media/")
    location = models.CharField(max_length=100,null=True,blank=True)
    like_by = models.ManyToManyField(user,related_name="like",blank=True)
    saved_by =models.ManyToManyField(user,related_name="save_post",blank=True)
    comments = models.JSONField(default=list,blank=True)

    def __str__(self):
        return f"{self.User.username}"


    
    