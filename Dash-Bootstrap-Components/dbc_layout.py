import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.Div([
        dbc.Row(dbc.Col(html.Div('A single column'))),
        dbc.Row([
            dbc.Col(html.Div("One of three columns")),
            dbc.Col(html.Div("One of three columns")),
            dbc.Col(html.Div("One of three columns")),
        ])
    ]),
    html.Br(),
    html.Div(
        [
            dbc.Row(dbc.Col(html.Div("A single, half-width column"), width=6)),
            dbc.Row(
                dbc.Col(html.Div("An automatically sized column"), width="auto")
            ),
            dbc.Row(
                [
                    dbc.Col(html.Div("One of three columns"), width=3),
                    dbc.Col(html.Div("One of three columns")),
                    dbc.Col(html.Div("One of three columns"), width=3),
                ]
            ),
        ]
    ),

    html.Br(),
    html.Div(
        [
            dbc.Row(
                dbc.Col(
                    html.Div("A single, half-width column"),
                    width={"size": 6, "offset": 3},
                )
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.Div("The last of three columns"),
                        width={"size": 3, "order": "last", "offset": 1},
                    ),
                    dbc.Col(
                        html.Div("The first of three columns"),
                        width={"size": 3, "order": 1, "offset": 2},
                    ),
                    dbc.Col(
                        html.Div("The second of three columns"),
                        width={"size": 3, "order": 12},
                    ),
                ]
            ),
        ]
    ),

    html.Br(),
    html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(html.Div("One of three columns"), md=4),
                    dbc.Col(html.Div("One of three columns"), md=4),
                    dbc.Col(html.Div("One of three columns"), md=4),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(html.Div("One of four columns"), width=6, lg=3),
                    dbc.Col(html.Div("One of four columns"), width=6, lg=3),
                    dbc.Col(html.Div("One of four columns"), width=6, lg=3),
                    dbc.Col(html.Div("One of four columns"), width=6, lg=3),
                ]
            ),
        ]
    ),

    html.Br(),
    dbc.Row(
        [
            dbc.Col(html.Div("One of three columns")),
            dbc.Col(html.Div("One of three columns")),
            dbc.Col(html.Div("One of three columns")),
        ],
        no_gutters=True,
    ),

    ##Vertical alignment
    html.Br(),
    html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(html.Div("One of three columns")),
                    dbc.Col(html.Div("One of three columns")),
                    dbc.Col(html.Div("One of three columns")),
                ],
                align="start",
            ),
            dbc.Row(
                [
                    dbc.Col(html.Div("One of three columns")),
                    dbc.Col(html.Div("One of three columns")),
                    dbc.Col(html.Div("One of three columns")),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(html.Div("One of three columns")),
                    dbc.Col(html.Div("One of three columns")),
                    dbc.Col(html.Div("One of three columns")),
                ],
                align="end",
            ),
            dbc.Row(
                [
                    dbc.Col(html.Div("One of three columns"), align="start"),
                    dbc.Col(html.Div("One of three columns"), align="center"),
                    dbc.Col(html.Div("One of three columns"), align="end"),
                ]
            ),
        ]
    ),

    #Horizontal alignment
    html.Br(),
    html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(html.Div("start"), width=4),
                    dbc.Col(html.Div("start"), width=4),
                ],
                justify="start",
            ),
            dbc.Row(
                [
                    dbc.Col(html.Div("center"), width=4),
                    dbc.Col(html.Div("center"), width=4),
                ],
                justify="center",
            ),
            dbc.Row(
                [
                    dbc.Col(html.Div("end"), width=4),
                    dbc.Col(html.Div("end"), width=4),
                ],
                justify="end",
            ),
            dbc.Row(
                [
                    dbc.Col(html.Div("between"), width=4),
                    dbc.Col(html.Div("between"), width=4),
                ],
                justify="between",
            ),
            dbc.Row(
                [
                    dbc.Col(html.Div("around"), width=4),
                    dbc.Col(html.Div("around"), width=4),
                ],
                justify="around",
            ),
        ]
    )

], className='mt-3')




if __name__ == '__main__':
    app.run_server(debug=True)