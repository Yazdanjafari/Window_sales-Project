from django.shortcuts import render
from .models import MeasurementForm
from Home_App.models import FirstShow
from django.http import HttpResponseRedirect

def measurement_show(request):
    if request.method == "POST":
        Full_Name_get = request.POST.get('Full_Name')
        Phone_Number_get = request.POST.get('Phone_Number')
        window_number_get = request.POST.get('window_number')
        door_number_get = request.POST.get('door_number')
        Lace_number_get = request.POST.get('Lace_number')
        Postal_ID_get = request.POST.get('Postal_ID')
        Address_get = request.POST.get('Address', None)
        
        if Full_Name_get and Phone_Number_get:
            MeasurementForm.objects.create(Full_Name=Full_Name_get,
                                           Phone_Number=Phone_Number_get,
                                           window_number=window_number_get,
                                           door_number=door_number_get,
                                           Lace_number=Lace_number_get,
                                           Address=Address_get)
            return HttpResponseRedirect("http://127.0.0.1:8000/Measurement/")
    
    FirstShow_info = FirstShow.objects.all()    
    return render(request, 'Measurement_App/Measurement.html', context={"FirstShow_info": FirstShow_info})


