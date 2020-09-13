import time

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

tab1_content = dbc.Card(
    dbc.CardBody([
        html.P("This is tab 1!", className='card-text'),
        dbc.Button('Click here', color='success'),
    ]),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 2!", className="card-text"),
            dbc.Button("Don't click here", color="danger"),
        ]
    ),
    className="mt-3",
)
app.layout = dbc.Container([
    dbc.Tabs([
        dbc.Tab(tab1_content, label='Tab 1'),
        dbc.Tab(tab2_content, label='Tab 2'),
        dbc.Tab(
            "This tab's content is never seen", label='Tab 3', disabled=True
        ),
    ]),

    html.Br(),
    html.Div(
        [
            dbc.Tabs(
                [
                    dbc.Tab(label="Tab 1", tab_id="tab-1"),
                    dbc.Tab(label="Tab 2", tab_id="tab-2"),
                ],
                id="tabs",
                active_tab="tab-1",
            ),
            html.Div(id="content"),
        ]
    ),

    html.Br(),
    dbc.Card([
        dbc.CardHeader(
            dbc.Tabs([
                dbc.Tab(label="Tab 1", tab_id="tab-1"),
                dbc.Tab(label="Tab 2", tab_id="tab-2"),
            ], id='card-tabs', card=True, active_tab='tab-1')
        ),
        dbc.CardBody(html.P(id="card-content", className="card-text")),
    ]),

    html.Br(),
    html.Div([
        dbc.Tabs(
            [
                dbc.Tab(label="Tab 1", tab_style={"margin-left": "auto"}),
                dbc.Tab(label="Tab 2", label_style={"color": "#00AEF9"}),
            ]
        ),
        html.Br(),
        dbc.Tabs(
            [
                dbc.Tab(label="Tab 1", tabClassName="ml-auto"),
                dbc.Tab(label="Tab 2", labelClassName="text-success"),
            ]
        ),
    ])

], className='mt-3')

@app.callback(
    Output("card-content", "children"), [Input("card-tabs", "active_tab")]
)
def tab_content(active_tab):
    return "This is tab {}".format(active_tab)


@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return tab1_content
    elif at == "tab-2":
        return tab2_content
    return html.P("This shouldn't ever be displayed...")

if __name__ == '__main__':
    app.run_server(debug=True)