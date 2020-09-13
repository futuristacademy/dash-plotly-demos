import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Jumbotron([
        html.H1('Jumbotron', className='display-3'),
        html.P(
            "Use a jumbotron to call attention to "
            "featured content or information.",
            className="lead",
        ),
        html.Hr(className="my-2"),
        html.P(
            "Jumbotrons use utility classes for typography and "
            "spacing to suit the larger container."
        ),
        html.P(dbc.Button("Learn more", color="primary"), className="lead"),
    ]),

    #fluid
    dbc.Jumbotron(
        [
            dbc.Container(
                [
                    html.H1("Fluid jumbotron", className="display-3"),
                    html.P(
                        "This jumbotron occupies the entire horizontal "
                        "space of its parent.",
                        className="lead",
                    ),
                    html.P(
                        "You will need to embed a fluid container in "
                        "the jumbotron.",
                        className="lead",
                    ),
                ],
                fluid=True,
            )
        ],
        fluid=True,
    )

], className='mt-3')




if __name__ == '__main__':
    app.run_server(debug=True)