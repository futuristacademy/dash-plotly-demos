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
import os

from pandas.tseries.offsets import *


# url = "https://raw.githubusercontent.com/uber-web/kepler.gl-data/master/earthquakes/data.csv"
# download_file = urllib.request.urlretrieve(url, "data.csv")
#

config = {
    'version': 'v1',
    'config': {
        'mapState': {
            'latitude': 35.9078,
            'longitude': 127.7669,
            'zoom': 6
        },
        'mapStyle': {
            'styleType': 'light'
        },
        'visState': {
            'layers': [{
                'type': 'hexagonId',
                # 'visualChannels': {
                #     'sizeField': {
                #         'type': 'integer',
                #         'name': 'value'
                #     },
                # },
                'config': {
                    'dataId': 'covid',
                    'color': [255, 0, 255]
                }
            }],
            'filters': [{
                'dataId': 'covid',
                'name': 'attributes.visited_date',
            }],
        }
    }
}


def make_kepler_plot(conn):
    q = conn.runInstalledQuery("getAllTravel")
    df = pd.json_normalize(q[0]['Seed'])
    # print(df)
    map_1 = keplergl.KeplerGl()
    map_1.add_data(data=df, name='covid')
    map_1.config = config
    map_1.save_to_html(file_name="covid_map.html")




def get_page(conn):
    # make plot
    if not os.path.isfile('Dash-Bootstrap-TigerGraph-Covid19/covid_map.html'):
        make_kepler_plot(conn)

    kep_viz = html.Iframe(srcDoc=open('covid_map.html').read(),
                        height='800', width='100%')

    kepler_page = html.Div(
        [
            html.H2("Kepler Visualization"),
            # dbc.Button('Submit', id='map-button', n_clicks=0),
            # html.Div(
            #     id='output-map'
            # )
            kep_viz
        ],
    )

    return kepler_page
