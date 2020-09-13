import time

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Toast(
        [html.P("This is the content of the toast", className="mb-0")],
        header="This is the header",  
    ),

    html.Br(),
    html.Div(
        [
            dbc.Button(
                "Open toast",
                id="simple-toast-toggle",
                color="primary",
                className="mb-3",
            ),
            dbc.Toast(
                [html.P("This is the content of the toast", className="mb-0")],
                id="simple-toast",
                header="This is the header",
                icon="primary",
                dismissable=True,
            ),
        ]
    ),

    html.Br(),
    html.Div(
        [
            dbc.Button(
                "Open toast",
                id="auto-toast-toggle",
                color="primary",
                className="mb-3",
            ),
            dbc.Toast(
                [html.P("This is the content of the toast", className="mb-0")],
                id="auto-toast",
                header="This is the header",
                icon="primary",
                duration=4000,
            ),
        ]
    ),

    html.Br(),
    html.Div(
        [
            dbc.Button(
                "Open toast", id="positioned-toast-toggle", color="primary"
            ),
            dbc.Toast(
                "This toast is placed in the top right",
                id="positioned-toast",
                header="Positioned toast",
                is_open=False,
                dismissable=True,
                icon="danger",
                # top: 66 positions the toast below the navbar
                style={"position": "fixed", "top": 66, "right": 10, "width": 350},
            ),
        ]
    )

], className='mt-3')

@app.callback(
    Output("simple-toast", "is_open"),
    [Input("simple-toast-toggle", "n_clicks")],
)
def open_toast(n):
    return True


@app.callback(
    Output("auto-toast", "is_open"), [Input("auto-toast-toggle", "n_clicks")]
)
def open_toast(n):
    return True

@app.callback(
    Output("positioned-toast", "is_open"),
    [Input("positioned-toast-toggle", "n_clicks")],
)
def open_toast(n):
    if n:
        return True
    return False


if __name__ == '__main__':
    app.run_server(debug=True)