from django.shortcuts import render
from .forms import AnomalyForm  
from .models import Detector, Anomaly, DetectAnomaly
def index_page(request):
    if request.method=="POST":
        if 'dec_id' in request.POST:
            d=Detector(id=request.POST['dec_id'], x_coord = request.POST['dec_x'], y_coord = request.POST['dec_y'])
        elif 'an_id' in request.POST:
            try:
                an_per = Anomaly.objects.get(id=request.POST['an_id'])
            except:
                an_per = Anomaly(id=request.POST['an_id'])
                # al.save()
                print(15)
            try:
                dec_per = Detector.objects.get(id=int(request.POST['an_dec_id']))
                dec_an = DetectAnomaly(detector_id = dec_per,anomaly_id=an_per,rate=float(request.POST['an_rate']))
            except:
                print('no_detector')
    context={}
    return render(request, 'index.html',context)

    