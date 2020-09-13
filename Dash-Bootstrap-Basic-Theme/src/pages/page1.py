import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import datetime
import numpy as np
import plotly.express as px

# START-HEATMAP-COMPONENT
np.random.seed(1)

programmers = ['Alex', 'Nicole', 'Sara', 'Etienne', 'Chelsea', 'Jody', 'Marianne']

base = datetime.datetime.today()
dates = base - np.arange(180) * datetime.timedelta(days=1)
z = np.random.poisson(size=(len(programmers), len(dates)))

fig2 = go.Figure(data=go.Heatmap(
        z=z,
        x=dates,
        y=programmers,
        colorscale='Viridis'))

fig2.update_layout(
    title='GitHub commits per day',
    xaxis_nticks=36,
    height=400)
# END-HEATMAP-COMPONENT
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop', height=400, title="Example Bar Chart")
# fig.update_layout(
#
# )


page1 = html.Div(
    [
        html.H2("Plotly Widgets 1"),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        dcc.Graph(figure=fig),
                        style={"height": "400px"},
                    ),
                    md=4,
                ),
                dbc.Col(
                    html.Div(
                        dcc.Graph(figure=fig2),
                        style={"height": "400px"},
                    ),
                    md=8,
                ),
            ],
            no_gutters=True,
        ),
        html.Br(),
        html.H4("Plotly Widgets 2"),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        cyto.Cytoscape(
                            id='cytoscape-compound',
                            layout={'name': 'preset'},
                            style={'width': '100%', 'height': '100%'},
                            stylesheet=[
                                {
                                    'selector': 'node',
                                    'style': {'content': 'data(label)'}
                                },
                                {
                                    'selector': '.countries',
                                    'style': {'width': 5}
                                },
                                {
                                    'selector': '.cities',
                                    'style': {'line-style': 'dashed'}
                                }
                            ],
                            elements=[
                                # Parent Nodes
                                {
                                    'data': {'id': 'us', 'label': 'United States'}
                                },
                                {
                                    'data': {'id': 'can', 'label': 'Canada'}
                                },

                                # Children Nodes
                                {
                                    'data': {'id': 'nyc', 'label': 'New York', 'parent': 'us'},
                                    'position': {'x': 100, 'y': 100}
                                },
                                {
                                    'data': {'id': 'sf', 'label': 'San Francisco', 'parent': 'us'},
                                    'position': {'x': 100, 'y': 200}
                                },
                                {
                                    'data': {'id': 'mtl', 'label': 'Montreal', 'parent': 'can'},
                                    'position': {'x': 400, 'y': 100}
                                },

                                # Edges
                                {
                                    'data': {'source': 'can', 'target': 'us'},
                                    'classes': 'countries'
                                },
                                {
                                    'data': {'source': 'nyc', 'target': 'sf'},
                                    'classes': 'cities'
                                },
                                {
                                    'data': {'source': 'sf', 'target': 'mtl'},
                                    'classes': 'cities'
                                }
                            ]
                        ),
                        style={"height": "300px", "border-style": "solid"},
                    ),
                    md=12,
                ),
                # dbc.Col(
                #     html.Div(
                #         "This is column 2",
                #         style={"height": "300px", "border-style": "solid"},
                #     ),
                #     md=6,
                # ),
            ],
            no_gutters=True,
        ),
    ]
)


def get_page1():
    return page1
