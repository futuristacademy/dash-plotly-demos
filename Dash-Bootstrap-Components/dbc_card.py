import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

card_content = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
    dbc.CardFooter('Card Footer'),
]

app.layout = dbc.Container([
    html.Div([
        dbc.Row([
            dbc.Col(dbc.Card(card_content, color="primary", inverse=True)),
            dbc.Col(
                dbc.Card(card_content, color="secondary", inverse=True)
            ),
            dbc.Col(dbc.Card(card_content, color="info", inverse=True)),
        ],className="mb-4",), 
        dbc.Row([
            dbc.Col(dbc.Card(card_content, color="success", inverse=True)),
            dbc.Col(dbc.Card(card_content, color="warning", inverse=True)),
            dbc.Col(dbc.Card(card_content, color="danger", inverse=True)),
        ],className="mb-4",),
        dbc.Row([
            dbc.Col(dbc.Card(card_content, color="light")),
            dbc.Col(dbc.Card(card_content, color="dark", inverse=True)),
        ],className="mb-4",)
    ]),

    html.Br(),
    html.Div([
        dbc.Row([
            dbc.Col(dbc.Card(card_content, color="primary", outline=True)),
            dbc.Col(
                dbc.Card(card_content, color="secondary", outline=True)
            ),
            dbc.Col(dbc.Card(card_content, color="info", outline=True)),
        ],className="mb-4",), 
        dbc.Row([
            dbc.Col(dbc.Card(card_content, color="success", outline=True)),
            dbc.Col(dbc.Card(card_content, color="warning", outline=True)),
            dbc.Col(dbc.Card(card_content, color="danger", outline=True)),
        ],className="mb-4",),
        dbc.Row([
            dbc.Col(dbc.Card(card_content, color="light", outline=True)),
            dbc.Col(dbc.Card(card_content, color="dark", outline=True)),
        ],className="mb-4",)
    ]),

    html.Br(),
    dbc.CardGroup([
        dbc.Card(
            dbc.CardBody([
                html.H5("Card 1", className="card-title"),
                html.P(
                    "This card has some text content, which is a little "
                    "bit longer than the second card.",
                    className="card-text",
                ),
                dbc.Button(
                    "Click here", color="success", className="mt-auto"
                ),
            ])
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Card 2", className="card-title"),
                    html.P(
                        "This card has some text content.",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Click here", color="warning", className="mt-auto"
                    ),
                ]
            )
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Card 3", className="card-title"),
                    html.P(
                        "This card has some text content, which is longer "
                        "than both of the other two cards, in order to "
                        "demonstrate the equal height property of cards in a "
                        "card group.",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Click here", color="danger", className="mt-auto"
                    ),
                ]
            )
        ),
    ]),

    html.Br(),
    dbc.CardDeck([
        dbc.Card(
            dbc.CardBody([
                html.H5("Card 1", className="card-title"),
                html.P(
                    "This card has some text content, which is a little "
                    "bit longer than the second card.",
                    className="card-text",
                ),
                dbc.Button(
                    "Click here", color="success", className="mt-auto"
                ),
            ])
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Card 2", className="card-title"),
                    html.P(
                        "This card has some text content.",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Click here", color="warning", className="mt-auto"
                    ),
                ]
            )
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Card 3", className="card-title"),
                    html.P(
                        "This card has some text content, which is longer "
                        "than both of the other two cards, in order to "
                        "demonstrate the equal height property of cards in a "
                        "card group.",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Click here", color="danger", className="mt-auto"
                    ),
                ]
            )
        ),
    ]),

    html.Br(),
    html.Div(
        [
            dbc.Card(
                dbc.CardBody("This is some text within a card body"),
                className="mb-3",
            ),
            dbc.Card("This is also within a body", body=True),
        ]
    ),

    html.Br(),
    html.Div([
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H4('Title', className='card-title'),
                        html.H6("Card subtitle", className="card-subtitle"),
                        html.P(
                            "Some quick example text to build on the card title and make "
                            "up the bulk of the card's content.",
                            className="card-text",
                        ),
                        dbc.CardLink('Card link', href='#'),
                        dbc.CardLink('External link', href='https://google.com'),
                    ]),
                ),
            ),
            dbc.Col(
                dbc.Card(
                    dbc.ListGroup([
                        dbc.ListGroupItem('Item 1'),
                        dbc.ListGroupItem("Item 2"),
                        dbc.ListGroupItem("Item 3"),
                    ], flush=True),
                    color='success',
                ),
            ),
            dbc.Col(
                dbc.Card([
                    dbc.CardHeader('This is the header'),
                    dbc.CardBody([
                        html.H4("Card title", className="card-title"),
                        html.P("This is some card text", className="card-text"),
                    ]),
                    dbc.CardFooter('This is the footer'),
                ]),
            ),
        ], className="mb-4",), 
    ]),

    html.Br(),
    html.Div(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5("75% width card", className="card-title"),
                        html.P(
                            [
                                "This card uses the ",
                                html.Code("w-75"),
                                " class to set the width to 75%",
                            ],
                            className="card-text",
                        ),
                    ]
                ),
                className="w-75 mb-3",
            ),
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5("50% width card", className="card-title"),
                        html.P(
                            [
                                "This card uses the ",
                                html.Code("w-50"),
                                " class to set the width to 50%",
                            ],
                            className="card-text",
                        ),
                    ]
                ),
                className="w-50",
            ),
        ]
    ),

    html.Br(),
    dbc.Row([
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardImg(src="./assets/placeholder286x180.png", top=True),
                    dbc.CardBody([
                        html.H5("Card title", className="card-title"),
                        html.P("This card has some text content, but not much else"),
                        dbc.Button("Go somewhere", color="primary"),
                    ]),
                ],
            ),
            width='4'
        ),

        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody([
                        html.H5("Card title", className="card-title"),
                        html.P(
                            "This card also has some text content and not much else, but "
                            "it is twice as wide as the first card."
                        ),
                        dbc.Button("Go somewhere", color="primary"),
                    ]),
                    dbc.CardImg(src="./assets/placeholder286x180.png", bottom=True),
                ],
            ),
            width='8'
        ),
    ]),

], className='mt-3 mb-10')

if __name__ == '__main__':
    app.run_server(debug=True)