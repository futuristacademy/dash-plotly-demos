import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

dropdown_menu_items = [
    dbc.DropdownMenuItem("Deep thought", id="dropdown-menu-item-1"),
    dbc.DropdownMenuItem("Hal", id="dropdown-menu-item-2"),
    dbc.DropdownMenuItem(divider=True),
    dbc.DropdownMenuItem("Clear", id="dropdown-menu-item-clear"),
]

app.layout = dbc.Container([
    html.Div([
        dbc.InputGroup([
            dbc.InputGroupAddon('@', addon_type='prepend'),
            dbc.Input(placeholder='Username'),
        ], className='mb-3'),
        dbc.InputGroup([
            dbc.Input(placeholder="Recipient's username"),
            dbc.InputGroupAddon("@example.com", addon_type="append"),
        ], className='mb-3'),
        dbc.InputGroup([
            dbc.InputGroupAddon('$', addon_type='prepend'),
            dbc.Input(placeholder='Amount', type='number'),
            dbc.InputGroupAddon('.00', addon_type='append'),
        ], className='mb-3'),
        dbc.InputGroup(
            [
                dbc.InputGroupAddon("With textarea", addon_type="prepend"),
                dbc.Textarea(),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.Select(
                    options=[
                        {"label": "Option 1", "value": 1},
                        {"label": "Option 2", "value": 2},
                    ]
                ),
                dbc.InputGroupAddon("With select", addon_type="append"),
            ]
        ),
    ]),

    html.Br(),
    #Size
    html.Div([
        dbc.InputGroup([
            dbc.InputGroupAddon('Large', addon_type='prepend'),
            dbc.Input(),
        ], size='lg'),
        html.Br(),
        dbc.InputGroup(
            [dbc.InputGroupAddon("Default", addon_type="prepend"), dbc.Input()]
        ),
        html.Br(),
        dbc.InputGroup(
            [dbc.InputGroupAddon("Small", addon_type="prepend"), dbc.Input()],
            size="sm",
        ),
    ]),

    html.Br(),
    html.Div([
        dbc.InputGroup([
            dbc.InputGroupAddon(dbc.RadioButton(), addon_type='prepend'),
            dbc.Input(),
        ],className='mb-3'),
        dbc.InputGroup([
            dbc.InputGroupAddon(dbc.Checkbox(), addon_type='prepend'),
            dbc.Input(),
        ])
    ]),

    html.Br(),
    dbc.InputGroup(
        [
            dbc.InputGroupAddon(
                dbc.Button("Random name", id="input-group-button"),
                addon_type="prepend",
            ),
            dbc.Input(id="input-group-button-input", placeholder="name"),
        ]
    ),

    html.Br(),
    dbc.InputGroup(
        [
            dbc.DropdownMenu(
                dropdown_menu_items, label="Generate", addon_type="prepend"
            ),
            dbc.Input(id="input-group-dropdown-input", placeholder="name"),
        ]
    ),

], className='mt-3')


@app.callback(
    Output("input-group-button-input", "value"),
    [Input("input-group-button", "n_clicks")],
)
def on_button_click(n_clicks):
    if n_clicks:
        names = ["Arthur Dent", "Ford Prefect", "Trillian Astra"]
        which = n_clicks % len(names)
        return names[which]
    else:
        return ""


@app.callback(
    Output("input-group-dropdown-input", "value"),
    [
        Input("dropdown-menu-item-1", "n_clicks"),
        Input("dropdown-menu-item-2", "n_clicks"),
        Input("dropdown-menu-item-clear", "n_clicks"),
    ],
)
def on_button_click(n1, n2, n_clear):
    ctx = dash.callback_context

    if not ctx.triggered:
        return ""
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "dropdown-menu-item-clear":
        return ""
    elif button_id == "dropdown-menu-item-1":
        names = ["Arthur Dent", "Ford Prefect", "Trillian Astra"]
        which = n1 % len(names)
        return names[which]
    else:
        names = ["David Bowman", "Frank Poole", "Dr. Heywood Floyd"]
        which = n2 % len(names)
        return names[which]

if __name__ == '__main__':
    app.run_server(debug=True)