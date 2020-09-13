import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.ListGroup([
        dbc.ListGroupItem('Item 1', active=True),
        dbc.ListGroupItem('Item 2'),
        dbc.ListGroupItem('Item 3'),
    ]),

    html.Br(),
    html.Div([
        dbc.ListGroup([
            dbc.ListGroupItem(
               "Internal link", href="/l/components/list_group" 
            ),
            dbc.ListGroupItem(
                "External link", href="https://google.com"
            ),
            dbc.ListGroupItem('Disable link', href='https://google.com', disabled=True),
            dbc.ListGroupItem(
                'Button', id='button-item', n_clicks=0, action=True
            )
        ]),
        html.P(id='counter'),
    ]),

    html.Br(),
    dbc.ListGroup(
        [
            dbc.ListGroupItem("The primary item", color="primary"),
            dbc.ListGroupItem("A secondary item", color="secondary"),
            dbc.ListGroupItem("A successful item", color="success"),
            dbc.ListGroupItem("A warning item", color="warning"),
            dbc.ListGroupItem("A dangerous item", color="danger"),
            dbc.ListGroupItem("An informative item", color="info"),
        ]
    ),

    html.Br(),
    dbc.ListGroup([
        dbc.ListGroupItem([
            dbc.ListGroupItemHeading('This item has a heading'),
            dbc.ListGroupItemText('And some text underneath'),
        ]),
        dbc.ListGroupItem([
            dbc.ListGroupItemHeading('This item also has a heading'),
            dbc.ListGroupItemText('And some more text underneath too')
        ])
    ]),

    html.Br(),
    html.Div(
        [
            dbc.ListGroup(
                [
                    dbc.ListGroupItem("Item 1"),
                    dbc.ListGroupItem("Item 2"),
                    dbc.ListGroupItem("Item 3"),
                ],
                horizontal=True,
                className="mb-2",
            ),
            dbc.ListGroup(
                [
                    dbc.ListGroupItem("Item 1"),
                    dbc.ListGroupItem("Item 2"),
                    dbc.ListGroupItem("Item 3"),
                ],
                horizontal="lg",
            ),
        ]
    )
], className='mt-3')

@app.callback(
    Output("counter", "children"), [Input("button-item", "n_clicks")]
)
def count_clicks(n):
    return f"Button clicked {n} times"


if __name__ == '__main__':
    app.run_server(debug=True)