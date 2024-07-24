from django.db import models
from django.utils import timezone

SocialMedia_choise =[
('ایمیل', 'ایمیل'), 
('اینستاگرام', 'اینستاگرام'),
('تلگرام', 'تلگرام'),
('لیندکدین', 'لیندکدین'),
('توییتر', 'توییتر'),
]

Desktop_img =[
('Reza', 'Reza'), 
('Defualt', 'Defualt'),
]

class Manager(models.Model):
    Profile_img = models.ImageField(upload_to="Personal")
    First_Name = models.CharField(max_length= 55)
    Last_Name = models.CharField(max_length= 55)
    Nationality_ID = models.CharField(max_length= 10)
    Birthday = models.DateField(help_text = "تاریخ تولد : مثال (12-12-1365)")
    Phone_Number = models.CharField(max_length= 11)
    Email = models.CharField(max_length= 255)
    info_about_your_work = models.CharField(max_length= 255, help_text = "توضیحاتی درمورد رزومه خود")
    desktop_photo = models.CharField(max_length= 55, choices = Desktop_img)
    def __str__(self):
        return f"{self.First_Name}  {self.Last_Name}"

class FirstShow(models.Model):
    line_1 = models.CharField(max_length= 55)
    line_2 = models.CharField(max_length= 55)
    line_3 = models.CharField(max_length= 55)

class WhyUPVC(models.Model):
    reason = models.CharField(max_length= 55)
    def __str__(self):
        return f"{self.reason}"    

class WhyChoose(models.Model):
    title_1 = models.CharField(max_length= 55)
    information_1 = models.CharField(max_length= 255)
    title_2 = models.CharField(max_length= 55)
    information_2 = models.CharField(max_length= 255)
    title_3 = models.CharField(max_length= 55)
    information_3 = models.CharField(max_length= 255)
    title_4 = models.CharField(max_length= 55)
    information_4 = models.CharField(max_length= 255)            

class BeforeBuyCost(models.Model):
    reason = models.CharField(max_length= 55)
    def __str__(self):
        return f"{self.reason}"
    
class BeforeBuyWhyWindowmall(models.Model):
    reason = models.CharField(max_length= 55)
    def __str__(self):
        return f"{self.reason}"
    
class BeforeBuyOrder(models.Model):
    reason = models.CharField(max_length= 55)
    def __str__(self):
        return f"{self.reason}"           

class SocialMedia(models.Model):
    Social_Media = models.CharField(max_length= 255, choices = SocialMedia_choise)
    Link = models.CharField(max_length= 255)
    def __str__(self):
        return f"{self.Social_Media}"    

class Request(models.Model):
    Full_Name = models.CharField(max_length= 55)
    Phone_Number = models.CharField(max_length= 11) 
    Description = models.CharField(max_length= 255, blank= True, null= True)
    created_time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.Full_Name}"    
