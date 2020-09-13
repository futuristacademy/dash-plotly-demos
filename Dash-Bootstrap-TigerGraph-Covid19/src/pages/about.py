import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

page = html.Div(
    [
        html.H2("About the Authors"),
        html.H5(""),
        html.H5('Akash Kaul'),
        dbc.Row(
            [
                dbc.Col(
                    html.H6(
                        dbc.Row(
                            [
                                html.I(className="fa fa-link"),
                                dcc.Link('Website', href='https://akashkaul.com', target="_blank")
                            ]
                        ),
                    ),
                    width=1
                ),
                dbc.Col(
                    html.H6(
                        dbc.Row(
                            [
                                html.I(className="fa fa-link"),
                                dcc.Link('LinkedIn', href='https://www.linkedin.com/in/akash-kaul-6a8063194/', target="_blank")
                            ]
                        ),
                    ),
                    width=1
                ),
                dbc.Col(
                    html.H6(
                        dbc.Row(
                            [
                                html.I(className="fa fa-link"),
                                dcc.Link('GitHub', href='https://github.com/akash-kaul', target="_blank")
                            ]
                        ),
                    ),
                    width=1
                ),
                dbc.Col(
                    html.H6(
                        dbc.Row(
                            [
                                html.I(className="fa fa-link"),
                                dcc.Link('Medium', href='https://medium.com/@akash_kaul', target="_blank")
                            ]
                        ),
                    ),
                    width=1
                ),
            ],
        ),
        html.H5(""),
        html.H5('Zrouga Mohamed'),
        dbc.Row(
            [
                dbc.Col(
                    html.H6(
                        dbc.Row(
                            [
                                html.I(className="fa fa-link"),
                                dcc.Link('Website', href='https://zrouga.com', target="_blank")
                            ]
                        ),
                    ),
                    width=1
                ),
                dbc.Col(
                    html.H6(
                        dbc.Row(
                            [
                                html.I(className="fa fa-link"),
                                dcc.Link('LinkedIn', href='https://www.linkedin.com/in/zrouga-mohamed/', target="_blank")
                            ]
                        ),
                    ),
                    width=1
                ),
                dbc.Col(
                    html.H6(
                        dbc.Row(
                            [
                                html.I(className="fa fa-link"),
                                dcc.Link('GitHub', href='https://github.com/zrouga-Mohamed', target="_blank")
                            ]
                        ),
                    ),
                    width=1
                ),
                dbc.Col(
                    html.H6(
                        dbc.Row(
                            [
                                html.I(className="fa fa-link"),
                                dcc.Link('Twitter', href='https://twitter.com/Zargonovski', target="_blank")
                            ]
                        ),
                    ),
                    width=1
                ),
            ],
        ),
        html.H5(""),
        html.H5('Jon Herke')
    ]
)


def get_page():
    return page
