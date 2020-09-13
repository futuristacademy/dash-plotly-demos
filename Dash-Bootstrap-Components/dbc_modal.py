import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

LOREM = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''

app.layout = dbc.Container([
    html.Div([
        dbc.Button('Open modal', id='open'),
        dbc.Modal([
            dbc.ModalHeader('Header'),
            dbc.ModalBody([
                dbc.InputGroup([
                    dbc.InputGroupAddon('Username', addon_type='prepend'),
                    dbc.Input(id='username', placeholder='Enter username'),
                ]),
                html.P(id='user-text'),
            ]),
            dbc.ModalFooter(
                dbc.Button('Close', id='close', className='ml-auto')
            ),
        ], id='modal')
    ]),

    html.Br(),
    html.Div(
        [
            dbc.Button("Small modal", id="open-sm", className="mr-1"),
            dbc.Button("Large modal", id="open-lg", className="mr-1"),
            dbc.Button("Extra large modal", id="open-xl"),
            dbc.Modal(
                [
                    dbc.ModalHeader("Header"),
                    dbc.ModalBody("A small modal."),
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-sm", className="ml-auto")
                    ),
                ],
                id="modal-sm",
                size="sm",
            ),
            dbc.Modal(
                [
                    dbc.ModalHeader("Header"),
                    dbc.ModalBody("A large modal."),
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-lg", className="ml-auto")
                    ),
                ],
                id="modal-lg",
                size="lg",
            ),
            dbc.Modal(
                [
                    dbc.ModalHeader("Header"),
                    dbc.ModalBody("An extra large modal."),
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-xl", className="ml-auto")
                    ),
                ],
                id="modal-xl",
                size="xl",
            ),
        ]
    ),

    html.Br(),
    html.Div(
        [
            dbc.FormGroup(
                [
                    dbc.Label("Backdrop:"),
                    dbc.RadioItems(
                        id="backdrop-selector",
                        options=[
                            {"label": "True (default)", "value": True},
                            {"label": "False", "value": False},
                            {"label": "'static'", "value": "static"},
                        ],
                        inline=True,
                        value=True,
                    ),
                ]
            ),
            dbc.Button("Open modal", id="open-backdrop"),
            dbc.Modal(
                [
                    dbc.ModalHeader("Header"),
                    dbc.ModalBody(
                        "Change the backdrop of this modal with the radio buttons"
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Close", id="close-backdrop", className="ml-auto"
                        )
                    ),
                ],
                id="modal-backdrop",
            ),
        ]
    ),

    html.Br(),
    html.Div(
        [
            dbc.Button("Scrolling modal", id="open-scroll", className="mr-1"),
            dbc.Button("Modal with scrollable body", id="open-body-scroll"),
            dbc.Modal(
                [
                    dbc.ModalHeader("Header"),
                    dbc.ModalBody(LOREM),
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-scroll", className="ml-auto")
                    ),
                ],
                id="modal-scroll",
            ),
            dbc.Modal(
                [
                    dbc.ModalHeader("Header"),
                    dbc.ModalBody(LOREM),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Close", id="close-body-scroll", className="ml-auto"
                        )
                    ),
                ],
                id="modal-body-scroll",
                scrollable=True,
            ),
        ]
    ),

    html.Br(),
    html.Div(
        [
            dbc.Button("Open", id="open-centered"),
            dbc.Modal(
                [
                    dbc.ModalHeader("Header"),
                    dbc.ModalBody("This modal is vertically centered"),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Close", id="close-centered", className="ml-auto"
                        )
                    ),
                ],
                id="modal-centered",
                centered=True,
            ),
        ]
    )

], className='mt-3')

def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output('user-text', 'children'),
    [Input('username', 'value')]
)
def enter_user(username):
    return f'Username is {username}'

app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)(toggle_modal)

@app.callback(
    Output("modal-backdrop", "backdrop"), [Input("backdrop-selector", "value")]
)
def select_backdrop(backdrop):
    return backdrop


app.callback(
    Output("modal-backdrop", "is_open"),
    [Input("open-backdrop", "n_clicks"), Input("close-backdrop", "n_clicks")],
    [State("modal-backdrop", "is_open")],
)(toggle_modal)




app.callback(
    Output("modal-sm", "is_open"),
    [Input("open-sm", "n_clicks"), Input("close-sm", "n_clicks")],
    [State("modal-sm", "is_open")],
)(toggle_modal)

app.callback(
    Output("modal-lg", "is_open"),
    [Input("open-lg", "n_clicks"), Input("close-lg", "n_clicks")],
    [State("modal-lg", "is_open")],
)(toggle_modal)

app.callback(
    Output("modal-xl", "is_open"),
    [Input("open-xl", "n_clicks"), Input("close-xl", "n_clicks")],
    [State("modal-xl", "is_open")],
)(toggle_modal)

app.callback(
    Output("modal-scroll", "is_open"),
    [Input("open-scroll", "n_clicks"), Input("close-scroll", "n_clicks")],
    [State("modal-scroll", "is_open")],
)(toggle_modal)

app.callback(
    Output("modal-body-scroll", "is_open"),
    [
        Input("open-body-scroll", "n_clicks"),
        Input("close-body-scroll", "n_clicks"),
    ],
    [State("modal-body-scroll", "is_open")],
)(toggle_modal)

app.callback(
    Output("modal-centered", "is_open"),
    [Input("open-centered", "n_clicks"), Input("close-centered", "n_clicks")],
    [State("modal-centered", "is_open")],
)(toggle_modal)

if __name__ == '__main__':
    app.run_server(debug=True)