from django.db import models
from django.utils import timezone

class MeasurementForm(models.Model):
    Full_Name = models.CharField(max_length= 55)
    Phone_Number = models.CharField(max_length= 11)
    window_number = models.IntegerField()
    door_number = models.IntegerField()
    Lace_number = models.IntegerField()
    Postal_ID = models.CharField(max_length= 15, blank= True, null= True)
    Address = models.CharField(max_length= 255)
    created_time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.Full_Name}"        

class Project (models.Model):
    Costumer_Name = models.CharField(max_length= 55)
    Costumer_Phone = models.CharField(max_length= 11)
    Costumer_Address = models.CharField(max_length= 255)
    window_number = models.IntegerField()
    door_number = models.IntegerField()
    Lace_number = models.IntegerField()
    Project_Price = models.IntegerField(help_text = "هزینه پروژه به تومان . مثال :‌ 10500000", blank= True, null= True)
    Measurement_Date = models.DateField(help_text = "تاریخ اندازه گیری : مثال (12-12-1365)", blank= True, null= True)
    Start_Date = models.DateField(help_text = "تاریخ شروع پروژه : مثال (12-12-1365)", blank= True, null= True)
    Finish_Date = models.DateField(help_text = "تاریخ پایان پروژه : مثال (12-12-1365)", blank= True, null= True)
    Description = models.CharField(max_length= 255, blank= True, null= True)        
    def __str__(self):
        return f"{self.Costumer_Name}"    