from django.db import models
from django.utils import timezone

class Installed(models.Model):
    title = models.CharField(max_length= 55)
    Installed_Img = models.ImageField(upload_to="Installed_Img", help_text = "لطفا سایز عکس یک در یک یا همان مربع باشد")
    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    Profile_img = models.ImageField(upload_to="Comment", blank= True, null= True)
    Full_Name = models.CharField(max_length= 55)
    Phone_Number = models.CharField(max_length= 11)
    description = models.CharField(max_length= 255)
    created_time = models.DateTimeField(default=timezone.now) 
    Active = models.BooleanField(default=False) 
    def __str__(self):
        if self.Active:
            return f"{self.Full_Name}  _  ✅"
        else:
            return f"{self.Full_Name}  _  ❌"
    

