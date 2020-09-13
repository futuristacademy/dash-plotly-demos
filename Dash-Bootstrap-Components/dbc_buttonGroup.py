import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.ButtonGroup(
        [dbc.Button('Left'), dbc.Button('Middle'), dbc.Button('Right')],
        size='lg',
        className='mr-1',
    ),
    dbc.ButtonGroup(
        [dbc.Button("Left"), dbc.Button("Middle"), dbc.Button("Right")],
        size="md",
        className="mr-1",
    ),
    dbc.ButtonGroup(
        [dbc.Button("Left"), dbc.Button("Middle"), dbc.Button("Right")],
        size="sm",
    ),

    html.Hr(),
    dbc.ButtonGroup([
        dbc.Button('First', color='success'),
        dbc.Button('Second', color='danger'),
        dbc.DropdownMenu(
            [dbc.DropdownMenuItem('Item 1'),
             dbc.DropdownMenuItem('Item 2')],
            label='Dropdown',
            group=True,
        )
    ]),

    html.Hr(),
    dbc.ButtonGroup([
        dbc.Button('First'),
        dbc.Button('Second'),
        dbc.DropdownMenu([
            dbc.DropdownMenuItem('Item 1'),
            dbc.DropdownMenuItem('Item 2'),
        ], label='Dropdown', group=True)
    ], vertical=True)

], className= 'mt-3')

if __name__ == '__main__':
    app.run_server(debug=True)