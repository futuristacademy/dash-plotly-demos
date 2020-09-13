import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

def make_popover(placement):
    return dbc.Popover(
        [
            dbc.PopoverHeader("Header"),
            dbc.PopoverBody(f"This is a {placement} popover"),
        ],
        id=f"popover-{placement}",
        target=f"popover-{placement}-target",
        placement=placement,
    )


def make_button(placement):
    return dbc.Button(
        f"Popover on {placement}",
        id=f"popover-{placement}-target",
        className="mx-2",
    )

app.layout = dbc.Container([
    html.Div([
        dbc.Button("Click to toggle popover", id="popover-target", color="danger"),
        dbc.Popover([
            dbc.PopoverHeader('Popover header'),
            dbc.PopoverBody("And here's some amazing content. Cool!"),
        ], id='popover', is_open=False, target='popover-target')
    ]),


    html.Br(),
    html.Div(
        [make_button(p) for p in ["top", "left", "right", "bottom"]]
        + [make_popover(p) for p in ["top", "left", "right", "bottom"]]
    )
], className='mt-3')


def toggle_popover(n, is_open):
    if n:
        return not is_open
    return is_open


app.callback(
    Output("popover", "is_open"),
    [Input("popover-target", "n_clicks")],
    [State("popover", "is_open")],
)(toggle_popover)

for p in ["top", "left", "right", "bottom"]:
    app.callback(
        Output(f"popover-{p}", "is_open"),
        [Input(f"popover-{p}-target", "n_clicks")],
        [State(f"popover-{p}", "is_open")],
    )(toggle_popover)

if __name__ == '__main__':
    app.run_server(debug=True)