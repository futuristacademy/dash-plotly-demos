import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Progress(value=50),
    html.Br(),
    dbc.Progress('25%', value=25),
    html.Br(),
    html.Div(
        [
            dbc.Progress(value=50, style={"height": "1px"}, className="mb-3"),
            dbc.Progress(value=50, style={"height": "30px"}),
        ]
    ),
    html.Br(),
    dbc.Progress(value=25, color="success", className="mb-3"),
    dbc.Progress(value=50, color="warning", className="mb-3"),
    dbc.Progress(value=75, color="danger", className="mb-3"),
    dbc.Progress(value=100, color="info", className='mb-3'),
    dbc.Progress(
        [
            dbc.Progress(value=20, color="success", bar=True),
            dbc.Progress(value=30, color="warning", bar=True),
            dbc.Progress(value=20, color="danger", bar=True),
        ],
        multi=True,
    ),

    html.Br(),
    dbc.Progress(value=75, striped=True),
    html.Br(),
    dbc.Progress(value=80, id="animated-progress", striped=True, animated=True),

    html.Br(),
    html.Div([
        dcc.Interval(id='progress-interval', n_intervals=0, interval=500),
        dbc.Progress(id='progress', color='success', animated=True),
    ])

], className='mt-3')


@app.callback(
     [Output("progress", "value"), Output("progress", "children")],
    [Input("progress-interval", "n_intervals")],
)
def update_progress(n):
    # check progress of some background process, in this example we'll just
    # use n_intervals constrained to be in 0-100
    progress = min(n % 110, 100)
    # only add text after 5% progress to ensure text isn't squashed too much
    return progress, f"{progress} %" if progress >= 5 else ""


if __name__ == '__main__':
    app.run_server(debug=True)