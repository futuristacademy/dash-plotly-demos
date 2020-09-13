import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "1.20rem 1rem",
    "background-color": "white",
}
tgLogoWhite = "https://info.tigergraph.com/hs-fs/hubfs/Logos/TigerGraph-whiteandgray.png?width=1545&name=TigerGraph-whiteandgray.png"
tgLogoOrange = 'https://www.tigergraph.com/wp-content/uploads/2018/03/tigergraph-logo-2color-cropped.png'

sidebar = html.Div(
    [
        # html.H2("Sidebar", className="display-4"),
        # html.H5("Dashboard"),
        html.Img(src=tgLogoOrange, height='50px', width='100%'),
        html.Hr(style={'margin-top': '1.25rem'}),
        # html.P(
        #     "A simple sidebar layout with navigation links", className="lead"
        # ),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.I(className="fa fa-id-card"),
                        " Patient",
                    ],
                    href="/page-1", id="page-1-link"
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa fa-globe"),
                        "  Global",
                    ],
                    href="/page-2", id="page-2-link"
                ),
                # dbc.NavLink("Global", href="/page-2", id="page-2-link"),
                dbc.NavLink(
                    [
                        html.I(className="fa fa-map"),
                        "  Map",
                    ],
                    href="/page-3", id="page-3-link"
                ),
                # dbc.NavLink("Map", href="/page-3", id="page-3-link"),
                dbc.NavLink(
                    [
                        html.I(className="fa fa-database"),
                        "  Data",
                    ],
                    href="/page-4", id="page-4-link"
                ),
                # dbc.NavLink("Data", href="/page-4", id="page-4-link"),
                dbc.NavLink(
                    [
                        html.I(className="fa fa-info-circle"),
                        "  About",
                    ],
                    href="/page-5", id="page-5-link"
                ),
                # dbc.NavLink("About", href="/page-5", id="page-5-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


def get_sidebar():
    return sidebar
