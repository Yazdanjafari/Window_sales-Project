from django.shortcuts import render
from .models import Installed, Comment
from Home_App.models import FirstShow
from django.http import HttpResponseRedirect

def cv_show(request):
    if request.method == "POST":
        Profile_img_get = request.FILES.get('Profile_img')
        Full_Name_get = request.POST.get('Full_Name')
        Phone_Number_get = request.POST.get('Phone_Number')        
        description_get = request.POST.get('comment', None)

        if Full_Name_get and Phone_Number_get:
            Comment.objects.create(Profile_img=Profile_img_get, Full_Name=Full_Name_get, Phone_Number=Phone_Number_get, description=description_get)    
            return HttpResponseRedirect("http://127.0.0.1:8000/CV/") 

    Installed_info = Installed.objects.all()
    Comment_info = Comment.objects.all()
    FirstShow_info = FirstShow.objects.all()
    
    return render(request, 'CV_App/CV.html', context={ "Installed_info": Installed_info,
                                                      "Comment_info": Comment_info,
                                                      "FirstShow_info": FirstShow_info})
