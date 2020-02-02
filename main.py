import pandas as pd
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

dash_app = dash.Dash()
app = dash_app.server

terror = pd.read_csv('./terrorism.csv')
col_options = [dict(label=x, value=x) for x in terror.columns]
dimensions = ["x", "y"]

app = dash_app.server

dash_app.layout = html.Div(children=[
    html.H1(children='Plot.ly Dash Example'),

    html.Div(children='''
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': terror['Year'], 'y': terror['Attacks'], 'type': 'line', 'name': u'Attacks'},
            ],
            'layout': {
                'title': 'Terrorist Attacks in the United States (1970-2017)'
            }
        }),
    dcc.Graph(
        figure={
            'data': [
                {'x': terror['Year'], 'y': terror['Deaths'], 'type': 'line', 'name': u'Deaths'},
            ],
            'layout': {
                'title': 'Terrorist Fatalities in the United States (1970-2017)'
            }
        }),
    dcc.Graph(
        figure={
            'data': [
                {'x': terror['Year'], 'y': terror['Injuries'], 'type': 'line', 'name': u'Injuries'},
            ],
            'layout': {
                'title': 'Terrorist Injuries in the United States (1970-2017)'
            }
        })

])

if __name__ == '__main__':
    dash_app.run_server(debug=True)