import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output, State
import pandas as pd
import keplergl
import geopandas as gpd
import urllib.request
# from dateutil.relativedelta import relativedelta
from pandas.tseries.offsets import *


url = "https://raw.githubusercontent.com/uber-web/kepler.gl-data/master/earthquakes/data.csv"
download_file = urllib.request.urlretrieve(url, "data.csv")

def make_kepler_plot():
    map_data = pd.read_csv("data.csv")
    map_1 = keplergl.KeplerGl()
    map_1.add_data(data=map_data)
    map_1.save_to_html(file_name="map_test.html")

# make plot
make_kepler_plot()

kep_viz = html.Iframe(srcDoc = open('map_test.html').read(), height='800', width='100%')

kepler_page = html.Div(
    [
        html.H2("Kepler Visualization"),
        kep_viz

    ]
)


def get_page():
    return kepler_page
