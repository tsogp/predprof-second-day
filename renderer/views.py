from django.shortcuts import render
from .forms import AnomalyForm  
from .models import Detector, Anomaly, DetectAnomaly

def generate():
    mas = Detector.objects.all()
    anomalies=Anomaly.objects.all()
    x=[]
    y=[]
    F={}
    bool_F={}
    for i in anomalies:
        F[i.id] = []
        bool_F[i.id] = []
    for i in mas:
        x.append(i.x_coord)
        y.append(i.y_coord)
        for k in F:
            # decs = DetectAnomaly.objects.get(detector_id=i.id,anomaly_id = k)
            try:
                decs = DetectAnomaly.objects.get(detector_id=i.id,anomaly_id = k)
                bool_F[k].append(True)
                F[k].append(decs.rate)
            except:
                F[k].append(-1)
                bool_F[k].append(False)
    return F,bool_F,x,y
    

def rasst(x, y):
    return((x**2 + y**2))

def find_detectors(): 
    F,exists,x,y=generate()
    n=0
    ot=[]
    for detector in F.keys():
        n+=1
        delta=1.024
        numsx=[]
        numsy=[]
        while (len(numsx)==0 or len(numsx)>2):
            numsx=[]
            numsy=[]
            numsk=[]
            delta*=0.8
            for x0 in range(1, 36):
                for y0 in range(1, 36):
                    flag=True
                    for f1 in range(len(F[detector])):
                        for f2 in range(f1+1, len(F[detector])):
                            if exists[detector][f1] and exists[detector][f2]:
                                r1=F[detector][f1]*rasst(x0-x[f1], y0-y[f1])
                                r2=F[detector][f2]*rasst(x0-x[f2], y0-y[f2])
                                if (abs(r2-r1)<=delta):
                                    numsx.append(x0)
                                    numsy.append(y0)
                                    numsk.append(r1)
        ot.append([numsx[0], numsy[0], round(numsk[0], 3)])
    return(ot)

def index_page(request):
    # print(find_detectors())
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

    