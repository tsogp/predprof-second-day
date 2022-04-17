from django.shortcuts import render
from .forms import AnomalyForm  
from .models import Detector, Anomaly, DetectAnomaly
def index_page(request):
    if request.method=="POST":
        if 'dec_id' in request.POST:
            d=Detector(id=request.POST['dec_id'], x_coord = request.POST['dec_x'], y_coord = request.POST['dec_y'])
        elif 'al_id' in request.POST:
            al = Anomaly(id=request.POST['an_id'])
            dec_an = DetectAnomaly(detector_id=request.POST['an_dec_id'],anomaly_id=request.POST['an_id'],rate=request.POST['an_rate'])
    context={}
    return render(request, 'index.html',context)

    