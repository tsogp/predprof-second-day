from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go


from .forms import AnomalyForm  
from .models import Detector, Anomaly, DetectAnomaly

SIZE = 10
def f(matrix, q, finish, point, current_way, current_value, been):
    # print(current_way)
    if point == finish:
        q.append((current_value, current_way))
        return

    if point[1] - 1 > 0 and not been[point[1] - 1][point[0]] and 0 < matrix[point[1] - 1][point[0]] < 2:
        new_point = (point[0], point[1] - 1)
        been[new_point[1]][new_point[0]] = True
        f(matrix, q, finish, new_point, current_way + [new_point], current_value + matrix[new_point[1]][new_point[0]], been)
        been[new_point[1]][new_point[0]] = False

    if point[0] - 1 > 0 and not been[point[1]][point[0] - 1] and 0 < matrix[point[1]][point[0] - 1] < 2:
        new_point = (point[0] - 1, point[1])
        been[new_point[1]][new_point[0]] = True
        f(matrix, q, finish, new_point, current_way + [new_point], current_value + matrix[new_point[1]][new_point[0]], been)
        been[new_point[1]][new_point[0]] = False

    if point[0] + 1 < SIZE and not been[point[1]][point[0] + 1] and 0 < matrix[point[1]][point[0] + 1] < 2:
        new_point = (point[0] + 1, point[1])
        been[new_point[1]][new_point[0]] = True
        f(matrix, q, finish, new_point, current_way + [new_point], current_value + matrix[new_point[1]][new_point[0]], been)
        been[new_point[1]][new_point[0]] = False

    if point[1] + 1 < SIZE and not been[point[1] + 1][point[0]] and 0 < matrix[point[1] + 1][point[0]] < 2:
        new_point = (point[0], point[1] + 1)
        been[new_point[1]][new_point[0]] = True
        f(matrix, q, finish, new_point, current_way + [new_point], current_value + matrix[new_point[1]][new_point[0]], been)
        been[new_point[1]][new_point[0]] = False


def find_way(matrix, start, finish):
    been = [[False] * SIZE for j in range(SIZE)]
    been[start[1]][start[0]] = True

    q = []

    f(matrix, q, finish, start, [start], matrix[start[1]][start[0]], been)
    # print(q)

    min_d = 999999
    ways = []
    for a in q:
        if a[0] < min_d:
            min_d = a[0]
            ways = [a[1]]
        elif a[0] == min_d:
            ways.append(a[1])

    min_len = 999999
    final_ways = []
    for w in ways:
        if len(w) < min_len:
            min_len = len(w)
            final_ways = [w]
        elif len(w) == min_len:
            final_ways.append(w)

    if len(final_ways) > 0:
        return final_ways[0]

    return []

    # print(find_way(matrix, start, finish))


def make_matrice(anomalies):
    ans = [[0 for i in range(0, 36)] for i in range(0, 36)]
    for anomaly in anomalies:
        for x in range(1, 36):
            for y in range(1, 36):
                if (x==anomaly[0] and y==anomaly[1]):
                    ans[x][y]=max(ans[x][y], anomaly[2])
                else:
                    ans[x][y] = max(ans[x][y], anomaly[2] / rasst(anomaly[0] - x, anomaly[1] - y) )
                ans[x][y]=round(ans[x][y], 1)
    return ans

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
    n = 0
    ot = []
    for detector in F.keys():
        n += 1
        delta = 1.024
        numsx = []
        numsy = []
        while (len(numsx) == 0 or len(numsx) > 2):
            numsx = []
            numsy = []
            numsk = []
            koef = 0
            delta *= 0.8
            for x0 in range(1, 36):
                for y0 in range(1, 36):
                    flag = True
                    for f1 in range(len(F[detector])):
                        for f2 in range(f1 + 1, len(F[detector])):
                            if exists[detector][f1] and exists[detector][f2]:
                                r1 = F[detector][f1] * rasst(x0 - x[f1], y0 - y[f1])
                                r2 = F[detector][f2] * rasst(x0 - x[f2], y0 - y[f2])
                                if (abs(r2 - r1) > delta):
                                    flag = False
                                    koef = r1
                    if flag:
                        numsx.append(x0)
                        numsy.append(y0)
                        numsk.append(koef)
        ot.append([numsx[0], numsy[0], round(numsk[0], 3)])
    '''schet = -1
    for i in F:
        schet+=1
        anom=Anomaly.objects.get(id=i)
        anom.center_x = ot[schet][0]
        anom.center_y = ot[schet][1]
        anom.real_rate = ot[schet][2]
        anom.save()'''
    return (ot)

def index_page(request):
    spis = []
    spis_x = []

    # print(find_detectors())
    find_detectors()
    if request.method=="POST":
        if 'dec_id' in request.POST:
            d=Detector(id=request.POST['dec_id'], x_coord = request.POST['dec_x'], y_coord = request.POST['dec_y'])
            d.save()
        elif 'an_id' in request.POST:
            try:
                an_per = Anomaly.objects.get(id=request.POST['an_id'])
            except:
                an_per = Anomaly(id=request.POST['an_id'])
                an_per.save()
            try:
                dec_per = Detector.objects.get(id=int(request.POST['an_dec_id']))
                dec_an = DetectAnomaly(detector_id = dec_per,anomaly_id=an_per,rate=float(request.POST['an_rate']))
                dec_an.save()
            except:
                print('no_detector')
        elif 'start_x' in request.POST:
            start_x = int(request.POST['start_x'])
            start_y = int(request.POST['start_y'])
            finish_x = int(request.POST['finish_x'])
            finish_y = int(request.POST['finish_y'])
            '''start_x+=1
            start_y+=1
            finish_x+=1
            finish_y+=1'''
            spis = find_way(make_matrice(find_detectors()),(start_x,start_y),(finish_x,finish_y))
            print(spis)
            spis_x=[]
            spis_y=[]
            for abra in spis:
                spis_x.append(abra[0])
                spis_y.append(abra[1])
    
    context = {}

    anomalies = Anomaly.objects.all()
    anomalies_x = []
    anomalies_y = []
    anomalies_name = []
    anomalies_rate = []
    anomalies_rate_text = []

    for i in range(len(anomalies)):
        print(anomalies[i].center_x, anomalies[i].center_y)
        anomalies_x.append(anomalies[i].center_x)
        anomalies_y.append(anomalies[i].center_y)
        anomalies_name.append(anomalies[i].id)
        anomalies_rate.append(anomalies[i].real_rate * 5)
        anomalies_rate_text.append('rate: ' + str(anomalies[i].real_rate))

    x = [i for i in range(0, 40 + 1)]
    y = [i for i in range(0, 40 + 1)]

    graphs = []
    print(spis_x)
    if spis_x:
        graphs.append(
            go.Scatter(x=spis_x, y=spis_y)
        )

    graphs.append(
        go.Scatter(
            x=anomalies_x, 
            y=anomalies_y, 
            mode='markers', 
            marker_size=anomalies_rate, 
            text=anomalies_rate_text,  
            marker={
                'color': ['rgb(255,105,180)'] * len(anomalies)
            },
        )
    )
    
    

    layout = {
        'title': 'Карта',
        'xaxis': {
            'side': 'top'
        },
        'yaxis': {
            'autorange': 'reversed'
        },
        'xaxis_title': 'X',
        'yaxis_title': 'Y',
        'images': [{
            'source': '/static/img/map.png',
            'xref': 'x',
            'yref': 'y',
            'x': 0,
            'y': 0,
            'sizex': 40,
            'sizey': 30,
            'sizing': 'stretch',
            'opacity': 1,
            'layer': 'below'
        }],
        'height': 1500,
        'width': 2000,
    }

    plot_div = plot({
        'data': graphs, 
        'layout': layout,
    }, output_type='div')
    
    context['plot_div'] = plot_div

    return render(request, 'index.html', context)

    