import time

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.Div(
        [
            dbc.Spinner(color="primary"),
            dbc.Spinner(color="secondary"),
            dbc.Spinner(color="success"),
            dbc.Spinner(color="warning"),
            dbc.Spinner(color="danger"),
            dbc.Spinner(color="info"),
            dbc.Spinner(color="light"),
            dbc.Spinner(color="dark"),
        ]
    ),

    html.Br(),
    html.Div([
        dbc.Button('Load', id='loading-button'),
        dbc.Spinner(html.Div(id='loading-output'), color='primary'),
    ]),

    html.Br(),
    html.Div(
        [
            dbc.Spinner(color="primary", type="grow"),
            dbc.Spinner(color="secondary", type="grow"),
            dbc.Spinner(color="success", type="grow"),
            dbc.Spinner(color="warning", type="grow"),
            dbc.Spinner(color="danger", type="grow"),
            dbc.Spinner(color="info", type="grow"),
            dbc.Spinner(color="light", type="grow"),
            dbc.Spinner(color="dark", type="grow"),
        ]
    ),

    html.Br(),
    html.Div(
        [
            dbc.Spinner(size="sm"),
            html.Hr(),
            dbc.Spinner(spinner_style={"width": "3rem", "height": "3rem"}),
        ]
    ),

    html.Br(),
    html.Div(
        [
            dbc.Button(
                dbc.Spinner(size="sm"),
                color="primary",
                disabled=True,
                className="mr-1",
            ),
            dbc.Button(
                [dbc.Spinner(size="sm"), " Loading..."],
                color="primary",
                disabled=True,
            ),
        ]
    ),

    html.Br(),
    html.Div(id='test_clicks', children=[
        dbc.Button(id='click_btn', color='primary'),
    ]),
    
], className='mt-3')

@app.callback(
    Output('test_clicks', 'children'),
    [Input('click_btn', 'n_clicks')],
    [State('test_clicks', 'children')]
)
def test(n_clicks, children):
    if n_clicks is None: 
        return children 
    else:
        print('Doing some calculation..') 
        time.sleep(3)

        new_element = dbc.Button(id='click_btn', color='success')

        children.pop()
        children.append(new_element)
        print('Generating a new button')
        return children

@app.callback(
    [Output('click_btn', 'children'),
     Output('click_btn', 'disabled'),],
    [Input('click_btn', 'n_clicks')],
)
def click(s):
    if s:
        return [dbc.Spinner(size="sm", color='secondary'), True]
    else:
        return ['Click Me', False]


@app.callback(
    Output('loading-output', 'children'),
    [Input('loading-button', 'n_clicks')]
)
def load_output(n):
    if n:
        time.sleep(1)
        return f'Output loaded {n} times'
    return "Output not reloaded yet"

if __name__ == '__main__':
    app.run_server(debug=True)