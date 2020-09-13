import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output, State

page2 = html.Div(
    [
        html.H2("This is page 2"),
    ]
)


def get_page2():
    return page2
