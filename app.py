# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:33:57 2020

@author: josep
"""

import pandas as pd
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

terror = pd.read_csv('./terrorism.csv')
col_options = [dict(label=x, value=x) for x in terror.columns]
dimensions = ["x", "y"]

app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)

app.layout = html.Div(
    [
        html.H1("US Terrorism Data from 1970 to 2017"),
        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ],
            style={"width": "25%", "float": "left"},
        ),
        dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"}),
    ]
)


@app.callback(Output("graph", "figure"), [Input(d, "value") for d in dimensions])
def make_figure(x, y):
    
    return px.line(terror, 
                   x=x, 
                   y=y, 
                   height=700)

app.run_server(debug=False)