import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import graphistry as graphistry 
from dash.dependencies import Input, Output, State
import pandas as pd
import urllib.request
from pandas.tseries.offsets import *

graphistry.register(api=3, protocol="https", server="hub.graphistry.com", username="jon.herke@tigergraph.com", password="2Bornot2B?")

url = "https://raw.githubusercontent.com/uber-web/kepler.gl-data/master/earthquakes/data.csv"
download_file = urllib.request.urlretrieve(url, "data.csv")

df = pd.read_csv("data.csv")
my_src_col = 'DateTime'
my_dest_col = 'EventID'

g = None
g = graphistry.edges(df).bind(source=my_src_col, destination=my_dest_col)
graph = g.plot()

graph_viz = html.Iframe(src=graph, height='800', width='100%')


graphistry_page = html.Div(
    [
        html.H2("Graphistry Visualization"),
        graph_viz
    ]
)


def get_page():
    return graphistry_page
