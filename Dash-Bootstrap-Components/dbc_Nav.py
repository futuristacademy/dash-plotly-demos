import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Nav([
        dbc.NavItem(dbc.NavLink('Active', active=True, href='#')),
        dbc.NavItem(dbc.NavLink('A link', href='#')),
        dbc.NavItem(dbc.NavLink('Another lilnk', href='#')),
        dbc.NavItem(dbc.NavLink('Disabled', disabled=True, href='#')),
        dbc.DropdownMenu([
            dbc.DropdownMenuItem(
                'google', href='https://www.google.com'
            ),
            dbc.DropdownMenuItem('Item 2'),
        ], label='Dropdown', nav=True)
    ]),

    html.Br(),
    dbc.Nav(
        [
            dbc.NavLink("Active", active=True, href="#"),
            dbc.NavLink("A link", href="#"),
            dbc.NavLink("Another link", href="#"),
            dbc.NavLink("Disabled", disabled=True, href="#"),
        ]
    ),

    html.Br(),
    html.Div([
        dbc.Nav([
            dbc.NavLink("Internal link", href="/l/components/nav"),
            dbc.NavLink("External link", href="https://github.com"),
            dbc.NavLink(
                "External relative",
                href="/l/components/nav",
                external_link=True,
            ),
            dbc.NavLink("Button", id="button-link", n_clicks=0),
        ]),
        html.Br(),
        html.P(id="button-clicks")
    ]),

    html.Br(),
    html.Div([
        dbc.Nav([
            dbc.NavItem(dbc.NavLink('A link', href='#')),
            dbc.NavItem(dbc.NavLink("Another link with a longer label", href="#")),
        ], justified=True),
        dbc.Nav([
            dbc.NavItem(dbc.NavLink('A link', href='#')),
            dbc.NavItem(dbc.NavLink("Another link with a longer label", href="#")),
        ], fill=True),
    ]),

    html.Br(),
    dbc.Nav(
        [
            dbc.NavItem(dbc.NavLink("Active", active=True, href="#")),
            dbc.NavItem(dbc.NavLink("A link", href="#")),
            dbc.NavItem(dbc.NavLink("Another link", href="#")),
            dbc.NavItem(dbc.NavLink("Disabled", disabled=True, href="#")),
        ],
        vertical="md",
    ),

    html.Br(),
    dbc.Nav(
        [
            dbc.NavItem(dbc.NavLink("Active", href="#")),
            dbc.NavItem(dbc.NavLink("A link", active=True, href="#")),
            dbc.NavItem(dbc.NavLink("Another link", href="#")),
            dbc.NavItem(dbc.NavLink("Disabled", disabled=True, href="#")),
        ],
        pills=True,
    ),
], className='mt-3')

@app.callback(
    Output("button-clicks", "children"), [Input("button-link", "n_clicks")]
)
def show_clicks(n):
    return "Button clicked {} times".format(n)


if __name__ == '__main__':
    app.run_server(debug=True)