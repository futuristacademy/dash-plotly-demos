import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

page1 = html.Div(
    [
        html.H2("Plotly Widgets 1"),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        "This is column 1",
                        style={"height": "100%", "border-style": "solid"},
                    ),
                    md=3,
                ),
                dbc.Col(
                    html.Div(
                        "This is column 2",
                        style={"height": "100%", "border-style": "solid"},
                    ),
                    md=6,
                ),
                dbc.Col(
                    html.Div(
                        "This is column 3",
                        style={"height": "100%", "border-style": "solid"},
                    ),
                    md=3,
                ),
            ],
            style={"height": "200px", "border-style": "solid"},
            no_gutters=True,
        ),
        html.Br(),
        html.H4("Plotly Widgets 2"),
        # dbc.Row(
        #     [
        #         dbc.Col(
        #             html.Div(
        #                 "This is column 1",
        #                 style={"height": "100px", "border-style": "solid"},
        #             ),
        #             md=3,
        #         ),
        #         dbc.Col(
        #             html.Div(
        #                 "This is column 2",
        #                 style={"height": "100px", "border-style": "solid"},
        #             ),
        #             md=6,
        #         ),
        #         dbc.Col(
        #             html.Div(
        #                 "This is column 3",
        #                 style={"height": "100px", "border-style": "solid"},
        #             ),
        #             md=3,
        #         ),
        #     ],
        #     no_gutters=True,
        # ),
        dbc.Col(
            html.Div(id="userInput", children=[
                dbc.Form([
                    dbc.FormGroup([
                        dbc.Input(id="userId", placeholder="Enter User ID", value="")
                    ]),
                    dbc.Button("Get Patient Info", id="userIdSubmit", n_clicks=0, color="primary", block=True)
                ]),
                html.Div(id="userIdOutput")
            ]),
            md=12,
        ),
    ]
)


def get_page1():
    return page1
