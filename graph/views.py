from django.shortcuts import render
from django.views.generic import TemplateView
import plotly.offline as opy
import plotly.graph_objs as go
import random
from django.http import JsonResponse
# import plotly.express as px

# Create your views here.

def home(request):
    print(bool(request.is_ajax))
    X=[random.randint(1,15) for i in range(0,10)]
    Y=[random.randint(1,15) for i in range(0,10)]
    Z=[random.randint(1,15) for i in range(0,10)]
    X2=[random.randint(1,15) for i in range(0,10)]
    Y2=[random.randint(1,15) for i in range(0,10)]
    Z2=[random.randint(1,15) for i in range(0,10)]
    X3=[random.randint(1,15) for i in range(0,10)]
    Y3=[random.randint(1,15) for i in range(0,10)]
    Z3=[random.randint(1,15) for i in range(0,10)]

    trace1 = go.Scatter3d(x=X, y=Y, z=Z, marker={'color':'red', 'symbol': 'circle'}, text='positive', mode='markers', name='red', hoverinfo="none")
    trace2 = go.Scatter3d(x=X2, y=Y2, z=Z2, marker={'color':'yellow', 'symbol': 'circle'}, text='negative', mode='markers', name='yellow', hoverinfo="none")
    trace3 = go.Scatter3d(x=X3, y=Y3, z=Z3, marker={'color':'blue', 'symbol': 'circle'}, text='Neutral', mode='markers', name='blue', hoverinfo="none")
    layout=go.Layout(title="Example")
    # fig = go.Figure(data=[trace1,trace2,trace3], layout=layout)
    fig = go.Figure(data=[], layout=layout)
    graph = fig.to_html(full_html=False, default_height=500, default_width=700)
    context = {'graph': graph}
    return render(request, 'graph/home.html', context)

def final(request):

    query=request.GET.get('q')
    if request.is_ajax and request.method == 'GET' and query=="load":
        X=[random.randint(1,15) for i in range(0,10)]
        Y=[random.randint(1,15) for i in range(0,10)]
        Z=[random.randint(1,15) for i in range(0,10)]
        X2=[random.randint(1,15) for i in range(0,10)]
        Y2=[random.randint(1,15) for i in range(0,10)]
        Z2=[random.randint(1,15) for i in range(0,10)]
        X3=[random.randint(1,15) for i in range(0,10)]
        Y3=[random.randint(1,15) for i in range(0,10)]
        Z3=[random.randint(1,15) for i in range(0,10)]

        trace1 = go.Scatter3d(x=X, y=Y, z=Z, marker={'color':'red', 'symbol': 'circle'}, text='positive', mode='markers', name='red', hoverinfo="none")
        trace2 = go.Scatter3d(x=X2, y=Y2, z=Z2, marker={'color':'yellow', 'symbol': 'circle'}, text='negative', mode='markers', name='yellow', hoverinfo="none")
        trace3 = go.Scatter3d(x=X3, y=Y3, z=Z3, marker={'color':'blue', 'symbol': 'circle'}, text='Neutral', mode='markers', name='blue', hoverinfo="none")
        layout=go.Layout(title="Example")
        fig = go.Figure(data=[trace1,trace2,trace3], layout=layout)
        graph = fig.to_html(full_html=False, default_height=500, default_width=700)
        context = {'graph': graph}
        return JsonResponse(context)

    # fig = go.Figure(data=[trace1,trace2,trace3], layout=layout)
    layout=go.Layout(title="Example")
    fig = go.Figure(data=[], layout=layout)
    graph = fig.to_html(full_html=False, default_height=400, default_width=400)
    context = {'graph': graph}
    return render(request, 'graph/final.html', context)


class Graph(TemplateView):
    template_name = 'graph/graph.html'

    def get_context_data(self, **kwargs):
        context = super(Graph, self).get_context_data(**kwargs)

        X=[random.randint(1,15) for i in range(0,10)]
        Y=[random.randint(1,15) for i in range(0,10)]
        Z=[random.randint(1,15) for i in range(0,10)]
        X2=[random.randint(1,15) for i in range(0,10)]
        Y2=[random.randint(1,15) for i in range(0,10)]
        Z2=[random.randint(1,15) for i in range(0,10)]
        X3=[random.randint(1,15) for i in range(0,10)]
        Y3=[random.randint(1,15) for i in range(0,10)]
        Z3=[random.randint(1,15) for i in range(0,10)]
        
        

        # Legend is used for naming each trace
        # Text for labeling each data
        # mode for showing relation between each data
        # text for giving identity/name to each data/trace(shows on hover)
        # hoverinfo shows data on hovering over the data

        trace1 = go.Scatter3d(x=X, y=Y, z=Z, marker={'color':'red', 'symbol': 'circle'}, text='positive', mode='markers', name='red', hoverinfo="none")
        trace2 = go.Scatter3d(x=X2, y=Y2, z=Z2, marker={'color':'yellow', 'symbol': 'circle'}, text='negative', mode='markers', name='yellow', hoverinfo="none")
        trace3 = go.Scatter3d(x=X3, y=Y3, z=Z3, marker={'color':'blue', 'symbol': 'circle'}, text='Neutral', mode='markers', name='blue', hoverinfo="none")
        data=go.Data([trace1,trace2,trace3])
        layout=go.Layout(title="Example", xaxis={'title':'x1'}, yaxis={'title':'x2'})
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['graph'] = div

        return context

