from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Manager, FirstShow, WhyUPVC, WhyChoose, BeforeBuyCost, BeforeBuyWhyWindowmall, BeforeBuyOrder, SocialMedia, Request

def home_show(request):
    if request.method == "POST":
        Full_Name_get = request.POST.get('Full_Name')
        Phone_Number_get = request.POST.get('Phone_Number')
        Description_get = request.POST.get('comment', None)

        if Full_Name_get and Phone_Number_get:
            Request.objects.create(Full_Name=Full_Name_get, Phone_Number=Phone_Number_get, Description=Description_get)    
            return HttpResponseRedirect("http://127.0.0.1:8000/")  # assuming 'home' is the name of the home URL pattern

    Manager_info = Manager.objects.all()
    FirstShow_info = FirstShow.objects.all()
    WhyUPVC_info = WhyUPVC.objects.all()
    WhyChoose_info = WhyChoose.objects.all()
    BeforeBuyCost_info = BeforeBuyCost.objects.all()
    BeforeBuyWhyWindowmall_info = BeforeBuyWhyWindowmall.objects.all()
    BeforeBuyOrder_info = BeforeBuyOrder.objects.all()
    SocialMedia_info = SocialMedia.objects.all()
    
    return render(request, 'Home_App/index.html', context={
        "Manager_info": Manager_info,
        "FirstShow_info": FirstShow_info,
        "WhyUPVC_info": WhyUPVC_info,
        "WhyChoose_info": WhyChoose_info,
        "BeforeBuyCost_info": BeforeBuyCost_info,
        "BeforeBuyWhyWindowmall_info": BeforeBuyWhyWindowmall_info,
        "BeforeBuyOrder_info": BeforeBuyOrder_info,
        "SocialMedia_info": SocialMedia_info,
    })