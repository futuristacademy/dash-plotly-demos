import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        html.Div([
            dbc.Button("Toggle", id='alert-toggle-auto', className='mr-1'),
            html.Hr(),
            dbc.Alert(
                "Hello! I am an auto-dismissing alert!",
                id="alert-auto",
                is_open=True,
                duration=2000,
            ),
        ]),

        html.Div([
            dbc.Button(
                "Toggle alert with fade", id='alert-toggle-fade', className="mr-1"
            ),
            dbc.Button("Toggle alert without fade", id='alert-toggle-no-fade'),
            html.Hr(),
            dbc.Alert(
                "Hello! I am an alert",
                id='alert-fade',
                dismissable=True,
                is_open=True,
            ),
            dbc.Alert(
               "Hello! I am an alert that doesn't fade in or out",
               id='alert-no-fade',
               dismissable=True,
               fade=False,
               is_open=True, 
            )
        ]),

        dbc.Alert("This is a primary alert", color="primary"),
        dbc.Alert("This is a secondary alert", color="secondary"),
        dbc.Alert("This is a success alert! Well done!", color="success"),
        dbc.Alert("This is a warning alert... be careful...", color="warning"),
        dbc.Alert("This is a danger alert. Scary!", color="danger"),
        dbc.Alert("This is an info alert. Good to know!", color="info"),
        dbc.Alert("This is a light alert", color="light"),
        dbc.Alert("This is a dark alert", color="dark"),
        dbc.Alert([
            'This is a primary alter with an ',
            html.A('example link', href='#', className='alert-link'),
        ], color='primary'),
        dbc.Alert([
            html.H4("Well done!", className='alert-heading'),
            html.P(
                "This is a success alert with loads of extra text in it. So much "
                "that you can see how spacing within an alert works with this "
                "kind of content."
            ),
            html.Hr(),
            html.P(
                "Let's put some more text down here, but remove the bottom margin",
                 className="mb-0",
            )
        ]),

        
    ],
    className='p-5',
)

@app.callback(
    Output("alert-auto", "is_open"),
    [Input("alert-toggle-auto", "n_clicks")],
    [State("alert-auto", "is_open")],
)
def toggle_alert(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output('alert-fade', 'is_open'),
    [Input('alert-toggle-fade', 'n_clicks')],
    [State('alert-fade', 'is_open')],
)
def toggle_alert(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("alert-no-fade", "is_open"),
    [Input("alert-toggle-no-fade", "n_clicks")],
    [State("alert-no-fade", "is_open")],
)
def toggle_alert_no_fade(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug=True)