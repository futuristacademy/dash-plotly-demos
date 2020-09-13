import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])



app.layout = dbc.Container([
    dbc.Form([
        dbc.FormGroup([
            dbc.Label('Email', html_for='example-email'),
            dbc.Input(type='email', id='example-email', placeholder='Enter email'),
            dbc.FormText(
                "Are you on email? You simply have to be these days",
                color="secondary",
            )
        ]),
        dbc.FormGroup([
            dbc.Label('Password', html_for='example-password'),
            dbc.Input(
                type='password',
                id='example-password',
                placeholder='Enter password',
            ),
            dbc.FormText(
                "A password stops mean people taking your stuff", color="secondary"
            )
        ])
    ]),

    #row
    html.Hr(),
    dbc.Form([
        dbc.FormGroup([
            dbc.Label("Email", html_for='example-email-row', width=2),
            dbc.Col(
                dbc.Input(
                    type='email', id='example-email-row', placeholder="Enter email"
                ),
                width=10,
            )
        ], row=True),

        dbc.FormGroup([
           dbc.Label("Password", html_for="example-password-row", width=2),
            dbc.Col(
                dbc.Input(
                    type="password",
                    id="example-password-row",
                    placeholder="Enter password",
                ),
                width=10,
            ), 
        ], row=True),

        dbc.FormGroup([
            dbc.Label('Radios', html_for='example-radios-row', width=2),
            dbc.Col(
                dbc.RadioItems(
                    id='example-radios-row',
                    options=[
                        {"label": "First radio", "value": 1},
                        {"label": "Second radio", "value": 2},
                        {
                            "label": "Third disabled radio",
                            "value": 3,
                            "disabled": True,
                        },
                    ]
                ),
                width=10,
            )
        ], row=True)
    ]),


    ##grid layout
    html.Hr(),
    dbc.Row(
        [
            dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("Email", html_for="example-email-grid"),
                        dbc.Input(
                            type="email",
                            id="example-email-grid",
                            placeholder="Enter email",
                        ),
                    ]
                ),
                width=6,
            ),
            dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("Password", html_for="example-password-grid"),
                        dbc.Input(
                            type="password",
                            id="example-password-grid",
                            placeholder="Enter password",
                        ),
                    ]
                ),
                width=6,
            ),
        ],
        form=True,
    ),

    ## inline form
    html.Hr(),
    dbc.Form(
        [
            dbc.FormGroup(
                [
                    dbc.Label("Email", className="mr-2"),
                    dbc.Input(type="email", placeholder="Enter email"),
                ],
                className="mr-3",
            ),
            dbc.FormGroup(
                [
                    dbc.Label("Password", className="mr-2"),
                    dbc.Input(type="password", placeholder="Enter password"),
                ],
                className="mr-3",
            ),
            dbc.Button("Submit", color="primary"),
        ],
        inline=True,
    ),

    ##Feedback
    html.Hr(),
    html.Div(
        [
            dbc.FormGroup(
                [
                    dbc.Label("Email"),
                    dbc.Input(id="email-input", type="email", value=""),
                    dbc.FormText("We only accept gmail..."),
                    dbc.FormFeedback(
                        "That looks like a gmail address :-)", valid=True
                    ),
                    dbc.FormFeedback(
                        "Sorry, we only accept gmail for some reason...",
                        valid=False,
                    ),
                ]
            )
        ]
    ),


    ## dcc
    html.Hr(),
    dbc.Form([
        dbc.FormGroup(
            [
                dbc.Label("Dropdown", html_for="dropdown"),
                dcc.Dropdown(
                    id="dropdown",
                    options=[
                        {"label": "Option 1", "value": 1},
                        {"label": "Option 2", "value": 2},
                    ],
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Slider", html_for="slider"),
                dcc.Slider(id="slider", min=0, max=10, step=0.5, value=3),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("RangeSlider", html_for="range-slider"),
                dcc.RangeSlider(id="range-slider", min=0, max=10, value=[3, 7]),
            ]
        )
    ])

], className='mt-3')

@app.callback(
    [Output("email-input", "valid"), Output("email-input", "invalid")],
    [Input("email-input", "value")],
)
def check_validity(text):
    if text:
        is_gmail = text.endswith("@gmail.com")
        return is_gmail, not is_gmail
    return False, False

if __name__ == '__main__':
    app.run_server(debug=True)