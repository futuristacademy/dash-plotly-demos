import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.Span([
        dbc.Badge("Primary", color='primary', className='mr-1'),
        dbc.Badge("Secondary", color="secondary", className="mr-1"),
        dbc.Badge("Success", color="success", className="mr-1"),
        dbc.Badge("Warning", color="warning", className="mr-1"),
        dbc.Badge("Danger", color="danger", className="mr-1"),
        dbc.Badge("Info", color="info", className="mr-1"),
        dbc.Badge("Light", color="light", className="mr-1"),
        dbc.Badge("Dark", color="dark"),
    ], className='mt-3'),

    html.Br(),
    html.Span([
        dbc.Badge("Primary", pill=True, color="primary", className="mr-1"),
        dbc.Badge("Secondary", pill=True, color="secondary", className="mr-1"),
        dbc.Badge("Success", pill=True, color="success", className="mr-1"),
        dbc.Badge("Warning", pill=True, color="warning", className="mr-1"),
        dbc.Badge("Danger", pill=True, color="danger", className="mr-1"),
        dbc.Badge("Info", pill=True, color="info", className="mr-1"),
        dbc.Badge("Light", pill=True, color="light", className="mr-1"),
        dbc.Badge("Dark", pill=True, color="dark"),
    ]),
    html.Br(),

    html.Span([
        dbc.Badge('Primary', href='#', color='primary', className='mr-1'),
        dbc.Badge("Secondary", href="#", color="secondary", className="mr-1"),
        dbc.Badge("Success", href="#", color="success", className="mr-1"),
        dbc.Badge("Warning", href="#", color="warning", className="mr-1"),
        dbc.Badge("Danger", href="#", color="danger", className="mr-1"),
        dbc.Badge("Info", href="#", color="info", className="mr-1"),
        dbc.Badge("Light", href="#", color="light", className="mr-1"),
        dbc.Badge("Dark", href="#", color="dark"),
    ]),

    html.Br(),
    dbc.Button([
        'Notifications', dbc.Badge('3', color='light', className='ml-1')
    ], color='danger', className='mt-5'),

    html.H1(["Example heading", dbc.Badge("New", className="ml-1")]),
    html.H2(["Example heading", dbc.Badge("New", className="ml-1")]),
    html.H3(["Example heading", dbc.Badge("New", className="ml-1")]),
    html.H4(["Example heading", dbc.Badge("New", className="ml-1")]),
    html.H5(["Example heading", dbc.Badge("New", className="ml-1")]),
    html.H6(["Example heading", dbc.Badge("New", className="ml-1")]),
])

if __name__ == '__main__':
    app.run_server(debug=True)