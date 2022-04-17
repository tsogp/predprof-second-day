from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go

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
    
    context = {}

    x = [i for i in range(0, 40 + 1)]
    y = [i for i in range(0, 30 + 1)]

    # List of graph objects for figure.
    # Each object will contain on series of data.
    graphs = []

    # Adding linear plot of y1 vs. x.
    graphs.append(
        go.Scatter(x=x, y=y)
    )

    # Setting layout of the figure.
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

    # Getting HTML needed to render the plot.
    plot_div = plot({
        'data': graphs, 
        'layout': layout,
    }, output_type='div')
    
    context['plot_div'] = plot_div

    return render(request, 'index.html', context)

    