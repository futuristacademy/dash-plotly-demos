import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

options = ['Get Bank Info', 'Get User Info']
bank_options = ['Visa', 'Bank of America', 'Mastercard', 'American Express 95']
callbackPage = html.Div(
    [
        html.H2("Dash Callbacks"),
        dcc.Dropdown(
            id='query-options-radio',
            options=[{'label': k, 'value': k} for k in options],
            value='Get Bank Info',
            searchable=False,
        ),
        # dcc.RadioItems(id='bank-options'),
        html.Br(),
        html.Div(id='display-result'),
        html.Div(id='user-input-dropdown'),
        html.Div(id='display-bank-options')
    ]
)


def get_page():
    return callbackPage
