from turtle import width
from django.shortcuts import render
import plotly
from plotly.offline import plot
import plotly.graph_objects as go
from sqlalchemy import create_engine
import pandas.io.sql as psql
import sqlalchemy as sq 
import pandas as pd 
import os 
from django.conf import settings
import json
# Create your views here.

def index(request):
    def scatter():
        conn = os.path.join(settings.BASE_DIR, 'static', 'assets','files' ,  'GDP.xlsx')
        df = pd.read_excel(conn)
        x1 = df['X']
        y1 = df['Y']

        trace = go.Scatter(
            x=x1,
            y=y1
        )
        layout = dict(
            title_text = "GDP GROWTH WITH RESPECT PER YEAR",
        )

        fig = go.Figure(data=[trace], layout=layout)
        plot_div = plot(fig, output_type='div')
        return plot_div

    def bar():
        x1 = ['Dar', "Mwanza", "Mbeya" , "Arusha" , "Dodoma" , "Tanga"]
        y1 = [100, 85, 70 , 63 , 57 , 45]

        trace = go.Bar(
            x=x1,
            y=y1
        )
        layout = dict(
            title_text = "TOP SIX REGIONS WITH THE HIGHEST GDP ",
        )

        fig = go.Figure(data=[trace], layout=layout)
        plot_div = plot(fig, output_type='div')
        return plot_div

    path = os.path.join(settings.BASE_DIR, 'static','assets', 'files',  'gdpdata.xlsx')
    df_2 = pd.read_excel(path)
    json_data = df_2.reset_index().to_json(orient='records')
    mydata = []
    mydata = json.loads(json_data)
    context = {
        'plot1': scatter(),
        'plot2' : bar(),
        'data' : mydata
    }

    return render(request , "partials/index.html" , context=context ) 