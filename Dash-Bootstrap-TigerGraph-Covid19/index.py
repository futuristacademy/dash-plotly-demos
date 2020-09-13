"""
This is a basic multi-page Dash app using Bootstrap.
"""
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_cytoscape as cyto
import src.components.navbar as nb
import src.components.sidebar as sb
import pyTigerGraph as tg
import plotly.express as px
import json
import pandas as pd
import connect
import threading

dataLock = threading.Lock()
conn = connect.getConnection()



import src.pages.patientView as p1
import src.pages.mapExplore as p3
import src.pages.dataStatistics as p4
import src.pages.globalView as p2
import src.pages.about as p5
import time 
from dash.dependencies import Input, Output, State
from datetime import datetime , timedelta 
from config import graphistry_un, graphistry_pw
import operator
import keplergl
import os

# link fontawesome to get the chevron icons
FA = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"

# setup stylesheets
app = dash.Dash(external_stylesheets=[dbc.themes.LUX, FA])

'''
TigerGraph Connection Parameters:
'''

# conn = connect.getConnection()
def Setup_pages(conn,graphistry_un,graphistry_pw):
    # setup parameters
    navbar = nb.get_navbar()
    sidebar = sb.get_sidebar()
    patientView = p1.get_page(conn)
    globalView = p2.get_page(conn,graphistry_un,graphistry_pw)
    mapView = p3.get_page(conn)
    dataView = p4.get_page(conn)
    aboutView = p5.get_page()
    return navbar , sidebar , patientView , globalView , mapView  , dataView ,  aboutView



# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}


def generateKeplerMap():
    q = conn.runInstalledQuery("getAllTravel")
    df = pd.json_normalize(q[0]['Seed'])
    # print(df)
    map_1 = keplergl.KeplerGl()
    map_1.add_data(data=df)
    if not os.path.isfile('Dash-Bootstrap-TigerGraph-Covid19/covid_map.html'):
        map_1.save_to_html(file_name="covid_map.html")
    else:
        os.remove('Dash-Bootstrap-TigerGraph-Covid19/covid_map.html')
        map_1.save_to_html(file_name="covid_map.html")

    kep_viz = html.Iframe(srcDoc=open('covid_map.html').read(),
                          height='800', width='100%')
    return kep_viz


@app.callback(Output('output-map', 'children'), [Input(component_id="map-button", component_property="n_clicks")])
def generateMap(n_clicks):
    if n_clicks > 0:
        try:
            map = generateMap()
            return map
        except Exception as e:
            return [html.Br(), html.P("Uh oh", style={'color': 'red'})]


def getPatientData(userID):
    q = conn.runInstalledQuery("getPatientInfo", {'p': userID})
    patientID = q[0]['Patient'][0]['v_id']
    patientSex = q[0]['Patient'][0]['attributes']['sex']
    patientBirthYear = q[0]['Patient'][0]['attributes']['birth_year']
    patientAge = datetime.now().year - patientBirthYear
    patientDeceased = False if q[0]['Patient'][0]['attributes']['deceased_date'].startswith(
        '1970') else True
    patientCountry = q[0]['Patient_Locations'][2]['v_id']
    patientProvince = q[0]['Patient_Locations'][0]['v_id']
    patientCity = q[0]['Patient_Locations'][1]['v_id']
    return patientID, patientSex, patientAge, patientDeceased, patientBirthYear, patientCountry, patientProvince, patientCity


def getPatientDates(userID):
    q = conn.runInstalledQuery("getPatientTimeline", {'p': userID})
    # print(str(q))
    # patientDates = []
    # patientDateLabels = []
    divs = []
    dates = []

    for x, y in q[0]['Seed'][0]['attributes'].items():
        # patientDateLabels.append(x)
        # patientDates.append(y)
        date = y.split(' ')[0].split('-')
        if date[0] != '1970':
            dates.append(
                [date[1], date[2], f"covid-19 | {x}", 'fa fa-medkit fa-lg', 'red'])
        # divs.append(
        #     html.H5(f"Date: {y.split(' ')[0]} ---- {x}")
        # )

    for event in q[0]['results']:
        # patientDates.append(event['attributes']['visited_date'])
        # patientDateLabels.append(event['attributes']['travel_type'])
        date = event['attributes']['visited_date'].split(' ')[0].split('-')
        if date[0] != '1970':
            dates.append(
                [date[1], date[2], f"travel event | {event['attributes']['travel_type']}", 'fa fa-plane fa-lg', 'black'])
        # divs.append(
        #     html.H5(f"Date: {event['attributes']['visited_date'].split(' ')[0]} ---- Travel Event : {event['attributes']['travel_type']}")
        # )
    dates.sort(key=operator.itemgetter(0, 1))
    # print(dates)
    for x in dates:
        # print(x[0], x[1])
        # f"Date: 2020-{x[0]}-{x[1]}"
        divs.append(
            dbc.Row(
                [
                    html.I(
                        className=f"{x[3]}",
                        style={'margin-left': '5px',
                               'margin-right': '5px', 'color': f"{x[4]}"},
                    ),
                    html.H5(
                        f"2020-{x[0]}-{x[1]} | {x[2]}",
                        # style={'color': f"{x[4]}"}
                    )
                ]
            )

        )
        divs.append(html.Hr(style={'margin': '0 0 1.24rem 0'}))

    return divs


def getPatientStats(userID):
    q = conn.runInstalledQuery("getPatientStats", {'p': userID})
    return [q[0]['TRAVEL_COUNT'], q[0]['CONTACT_COUNT'], q[0]['INFECTION_COUNT'], q[0]['RISK_SCORE']]


@app.callback([Output('travel-counter-div', 'children'), Output('contact-counter-div', 'children'), Output('infection-counter-div', 'children'), Output('risk-score-div', 'children')], [Input(component_id="input-group-button", component_property="n_clicks")], [State("input-group-button-input", "value")])
def getpatientStats(n_clicks, userID):
    if n_clicks != 0:
        try:
            results = getPatientStats(userID)
            return [html.Div(
                [
                    html.P('Travel Events'),
                    html.Br(),
                    html.H2(results[0]),

                ],
            ),
                html.Div(
                [
                    html.P('People Encountered'),
                    html.Br(),
                    html.H2(results[1]),
                ]
            ),
                html.Div(
                [
                    html.P('People Infected'),
                    html.Br(),
                    html.H2(results[2]),
                ]
            ),
                html.Div(
                [
                    html.P('Risk Score'),
                    html.Br(),
                    html.H2(results[3]),
                ]
            )]
        except Exception as e:
            return html.P("Error", style={'color': 'red'}), html.P("Error", style={'color': 'red'}), html.P("Error", style={'color': 'red'}), html.P("Error", style={'color': 'red'})


@ app.callback(Output('timeline-div', 'children'), [Input(component_id="input-group-button", component_property="n_clicks")], [State("input-group-button-input", "value")])
def getPatientTimeline(n_clicks, userID):
    if n_clicks != 0:
        try:
            divs = getPatientDates(userID)
            patientTimeline = html.Div(
                children=divs
            )
            return patientTimeline
        except Exception as e:
            return [html.Br(), html.P("Please enter Valid Patient ID", style={'color': 'red'})]


@app.callback(Output("output-panel", "children"), [Input(component_id="input-group-button", component_property="n_clicks")], [State("input-group-button-input", "value")])
def getPatientInfo(n_clicks, userID):
    if n_clicks != 0:
        try:
            id, sex, age, deceased, birthYear, country, province, city = getPatientData(
                userID)
            dec = 'T' if deceased else 'F'
            sex = sex.upper()
            patientData = html.Div(
                [
                    # dbc.Row(
                    #     [
                    #         html.H6('Patient ID :'),
                    #         html.P(f'{id}')
                    #     ],
                    #     style={'text-align': 'center'}
                    # ),
                    # dbc.Row(
                    #     [
                    #         html.B('Sex :'),
                    #         html.P(f'{sex} '),
                    #         html.B('Age :'),
                    #         html.P(f'{age} '),
                    #         html.B('DOB :'),
                    #         html.P(f'{birthYear} '),
                    #         html.B('Deceased :'),
                    #         html.P(f'{dec}'),
                    #     ],
                    # ),
                    # dbc.Row(
                    #     [
                    #         html.B('Country :'),
                    #         html.P(f'{country} '),
                    #         html.B('Province :'),
                    #         html.P(f'{province} '),
                    #         html.B('City :'),
                    #         html.P(f'{city} '),
                    #     ],
                    # )

                    html.P(f'Patient ID: {id}'),
                    html.P(
                        f'Sex: {sex} Age: {age} DOB: {birthYear} Deceased: {dec}'),
                    html.P(
                        f'Country: {country} Province: {province} City: {city}'),
                ],
                style={'height': '100%', 'width': '100%',
                       'padding': '5px 0 0 0'},
            )
            return patientData
        except Exception as e:
            return [html.Br(), html.P("Please enter Valid Patient ID", style={'color': 'red'})]


def getPatientSubgraph(userID):
    q = conn.runInstalledQuery("infectionSubgraph", {'p': userID})
    # print(q)
    nodes = []
    edges = []
    for data in q[0]['@@edgeSet']:
        nodes.append(
            {'data':
             {'id': data['from_id'], 'label': data['from_type']}
             }
        )
        nodes.append(
            {'data':
             {'id': data['to_id'], 'label': data['to_type']}
             }
        )
        edges.append(
            {'data':
             {'source': data['from_id'], 'target': data['to_id']}
             }
        )
    # elements = list(nodes) + list(edges)
    elements = nodes + edges
    return elements


@app.callback(Output("subgraph-div", "children"), [Input(component_id="input-group-button", component_property="n_clicks")], [State("input-group-button-input", "value")])
def getpatientSubgraph(n_clicks, userID):
    if n_clicks != 0:
        try:
            elements = getPatientSubgraph(userID)
            graph = cyto.Cytoscape(
                id='patient-infection-subgraph',
                elements=elements,
                style={'width': '100%', 'height': '100%'},
                layout={
                    'name': 'cose'
                }
            )
            return graph
        except Exception as e:
            return [html.Br(), html.P("Error", style={'color': 'red'})]


# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 6)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False, False, False
    return [pathname == f"/page-{i}" for i in range(1, 6)]

global globalView
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return patientView
    elif pathname == "/page-2":
        return globalView
    elif pathname == "/page-3":
        return mapView
    elif pathname == "/page-4":
        return dataView
    elif pathname == "/page-5":
        return aboutView

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    print("===================== STARTED =====================================")
    start_time = time.time()
    navbar , sidebar , patientView , globalView , mapView  , dataView ,  aboutView = Setup_pages(conn,graphistry_un,graphistry_pw)
    content = html.Div(id="page-content", style=CONTENT_STYLE)
    app.layout = html.Div([dcc.Location(id="url"), navbar, sidebar, content])
    print("Fully loaded in ::   {}".format(str(timedelta(seconds=(time.time()-start_time)))))
    print("--------------------------------------------------------")
    app.run_server(port=8881, debug=True)#, dev_tools_hot_reload=True)
