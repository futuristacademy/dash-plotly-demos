import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

page2 = html.Div(
    [
        html.H2("Plotly Widgets 1"),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        "This is column 1",
                        style={"height": "300px", "border-style": "solid"},
                    ),
                    md=6,
                ),
                dbc.Col(
                    html.Div(
                        "This is column 2",
                        style={"height": "300px", "border-style": "solid"},
                    ),
                    md=6,
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
                        "This is column 1",
                        style={"height": "300px", "border-style": "solid"},
                    ),
                    md=6,
                ),
                dbc.Col(
                    html.Div(
                        "This is column 2",
                        style={"height": "300px", "border-style": "solid"},
                    ),
                    md=6,
                ),
            ],
            no_gutters=True,
        ),
    ]
)

def get_page2():
    return page2

    # dbc.Card(
    #                         [
    #                         dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
    #                         dbc.CardBody(
    #                             [
    #                                 html.H4("Card title", className="card-title"),
    #                                 html.P(
    #                                     "Some quick example text to build on the card title and "
    #                                     "make up the bulk of the card's content.",
    #                                     className="card-text",
    #                                 ),
    #                                 dbc.Button("Go somewhere", color="primary"),
    #                             ]
    #                             ),
    #                         ],
    #                     style={"width": "18rem"},
    #                     ),