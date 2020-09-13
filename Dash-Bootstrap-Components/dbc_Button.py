import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.Div([
        dbc.Button('Click me', color='success', id='example-button', className='mr-2'),
        html.Span(id='example-output', style={"vertical-algin": 'middle'}),
    ]),

    html.Br(),
    html.Div([
        dbc.Button('Primary', color='primary', className='mr-1'),
        dbc.Button("Secondary", color="secondary", className="mr-1"),
        dbc.Button("Success", color="success", className="mr-1"),
        dbc.Button("Warning", color="warning", className="mr-1"),
        dbc.Button("Danger", color="danger", className="mr-1"),
        dbc.Button("Info", color="info", className="mr-1"),
        dbc.Button("Light", color="light", className="mr-1"),
        dbc.Button("Dark", color="dark", className="mr-1"),
        dbc.Button("Link", color="link"),
    ]),

    html.Br(),
    html.Div([
        dbc.Button("Primary", outline=True, color='primary', className='mr-1'),
        dbc.Button(
            "Secondary", outline=True, color="secondary", className="mr-1"
        ),
        dbc.Button("Success", outline=True, color="success", className="mr-1"),
        dbc.Button("Warning", outline=True, color="warning", className="mr-1"),
        dbc.Button("Danger", outline=True, color="danger", className="mr-1"),
        dbc.Button("Info", outline=True, color="info", className="mr-1"),
        dbc.Button("Light", outline=True, color="light", className="mr-1"),
        dbc.Button("Dark", outline=True, color="dark"),
    ]),

    html.Br(),
    html.Div([
        dbc.Button('Large button', size='lg', className='mr-1'),
        dbc.Button("Regular button", className="mr-1"),
        dbc.Button("Small button", size="sm"),
    ]),

    html.Br(),
    dbc.Button("Block button", color="primary", block=True),

    html.Br(),
    html.Div([
        dbc.Button('Regular', color='success', className='mr-1'),
        dbc.Button("Active", color="success", active=True, className="mr-1"),
        dbc.Button("Disabled", color="success", disabled=True),
    ])

], className='mt-5')

@app.callback(
    Output('example-output', 'children'),
    [Input('example-button', 'n_clicks')]
)
def on_button_click(n):
    if n is None:
        return "Not clicked."
    else:
        return f"Clicked {n} times."

if __name__ == '__main__':
    app.run_server(debug=True)