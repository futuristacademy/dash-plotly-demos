import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.Div([
        dbc.Input(id='input', placeholder='Type something...', type='text'),
        html.Br(),
        html.P(id="output"),
    ]),

    ##number input
    html.Hr(),
    html.Div(
        [
            html.P("Type a number outside the range 0-10"),
            dbc.Input(type="number", min=0, max=10, step=1),
        ],
        id="styled-numeric-input",
    ),

    ##Label
    dbc.FormGroup(
        [
            dbc.Label("Text"),
            dbc.Input(placeholder="Input goes here...", type="text"),
            dbc.FormText("Type something in the box above"),
        ]
    ),

    ##Size
    html.Div(
        [
            dbc.Input(
                placeholder="A large input...", bs_size="lg", className="mb-3"
            ),
            dbc.Input(
                placeholder="A medium input...", bs_size="md", className="mb-3"
            ),
            dbc.Input(placeholder="A small input...", bs_size="sm"),
        ]
    ),

    html.Br(),

    ##validation
    html.Div([
        dbc.Input(placeholder='Valid input...', valid=True, className='mb-3'),
        dbc.Input(placeholder='Invalid input...', invalid=True)
    ]),

    ##textarea
    html.Br(),
    html.Div(
        [
            dbc.Textarea(className="mb-3", placeholder="A Textarea"),
            dbc.Textarea(
                valid=True,
                bs_size="sm",
                className="mb-3",
                placeholder="A small, valid Textarea",
            ),
            dbc.Textarea(
                invalid=True, bs_size="lg", placeholder="A large, invalid Textarea"
            ),
        ]
    ),

    ##select
    html.Br(),
    dbc.Select(
        id="select",
        options=[
            {"label": "Option 1", "value": "1"},
            {"label": "Option 2", "value": "2"},
            {"label": "Disabled option", "value": "3", "disabled": True},
        ],
    )

], className='mt-3')

@app.callback(Output("output", "children"), [Input("input", "value")])
def output_text(value):
    return value

if __name__ == '__main__':
    app.run_server(debug=True)