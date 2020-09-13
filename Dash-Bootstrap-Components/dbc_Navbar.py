import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

app.layout = dbc.Container([
    dbc.NavbarSimple([
        dbc.NavItem(dbc.NavLink('Page 1', href='#')),
        dbc.DropdownMenu([
            dbc.DropdownMenuItem('More pages', header=True),
            dbc.DropdownMenuItem('page 2', href='#'),
            dbc.DropdownMenuItem('page 3', href='#')
        ], nav=True, in_navbar=True, label='More')
    ], brand='NavbarSimple', brand_href='#', color='primary', dark=True),


    html.Br(),
    dbc.Navbar([
        html.A(
            dbc.Row([
                dbc.Col(html.Img(src=PLOTLY_LOGO, height='30px')),
                dbc.Col(dbc.NavbarBrand('Navbar', className='ml-2')),
            ], align='center', no_gutters=True),
            href="https://plot.ly",
        ),
        dbc.NavbarToggler(id='navbar-toggler'),
        dbc.Collapse(id="navbar-collapse", navbar=True, children=[
            dbc.Row(
                [
                    dbc.Col(dbc.Input(type="search", placeholder="Search")),
                    dbc.Col(
                        dbc.Button("Search", color="primary", className="ml-2"),
                        width="auto",
                    ),
                ],
                no_gutters=True,
                className="ml-auto flex-nowrap mt-3 mt-md-0",
                align="center",
            )
        ]),
    ], color='dark', dark=True)
    
], className='mt-3')

# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug=True)