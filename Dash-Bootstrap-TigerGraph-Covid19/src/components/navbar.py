import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
TG_LOGO = 'https://info.tigergraph.com/hs-fs/hubfs/Logos/TigerGraph-whiteandgray.png?width=1545&name=TigerGraph-whiteandgray.png'

right_elements = html.Div(
    children=[
        dbc.NavItem(dbc.NavLink("About", href="/page-5")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Patient", href="/page-1"),
                dbc.DropdownMenuItem("Global", href="/page-2"),
                dbc.DropdownMenuItem("Map", href="/page-3"),
                dbc.DropdownMenuItem("Data", href="/page-4"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
            right=True,
        ),
    ],
)

# navbar = dbc.Navbar(
#     [
#         html.A(
#             dbc.Row(
#                 [
#                     dbc.Col(html.Img(src=TG_LOGO, height='50px'), width=3),
#                     dbc.Col(html.Div(), width=6),
#                     dbc.Col(right_elements, width=3),
#                 ],
#                 style={'width': '100%'},
#             ),
#         ),
#     ],
#     color='orange',
#     dark=True,
# )
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("About", href="/page-5")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Patient", href="/page-1"),
                dbc.DropdownMenuItem("Global", href="/page-2"),
                dbc.DropdownMenuItem("Map", href="/page-3"),
                dbc.DropdownMenuItem("Data", href="/page-4"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
            right=True,
        ),
    ],
    brand="Covid-19 Dashboard",
    style={'margin-left': '16rem'},
    brand_href="#",
    color='#ef6c00',
    dark=False,
    fluid=True,
    # fixed='top',
)


def get_navbar():
    return navbar
