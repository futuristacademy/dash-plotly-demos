"""
This is a basic multi-page Dash app using Bootstrap.
"""
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import src.components.navbar as nb
import src.components.sidebar as sb
import pyTigerGraph as tg
import plotly.express as px
import json
import pandas as pd
import src.pages.page1 as p1
import src.pages.page2 as p2
import src.pages.kepler_page as kepler
import src.pages.callbackPage as callbackPage
import src.pages.graphistry_page as graphistry
from dash.dependencies import Input, Output, State

# link fontawesome to get the chevron icons
FA = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"

# setup stylesheets
app = dash.Dash(external_stylesheets=[dbc.themes.LUX, FA])

# setup parameters
navbar = nb.get_navbar()
sidebar = sb.get_sidebar()
page1 = p1.get_page1()
page2 = p2.get_page2()
kepler_page = kepler.get_page()
callbackPage = callbackPage.get_page()
graphistry_page = graphistry.get_page()


'''
TigerGraph Connection Parameters:
'''

hostname = "https://payment-fraud.i.tgcloud.io"
username = "tigergraph"
graphname = "MyGraph"
password = "tigergraph"
# conn = None
try:
    conn = tg.TigerGraphConnection(host=hostname,
                                   graphname=graphname,
                                   username=username,
                                   password=password,
                                   useCert=True)
    secret = conn.createSecret()
    token = conn.getToken(secret, setToken=True)

    # print(conn.gsql('ls'))
except Exception as e:
    print('There was an error. Make sure to start your box and try again')


def getUserInfo(userID):
    q = conn.runInstalledQuery("getUserInfo", {'userID': userID})
    userAccount = q[0]['S1'][0]['v_id']
    # userEmail = q[0]['S1'][1]['v_id']
    userEmail = ""
    userPhone = ""
    for x in q[0]['S1']:
        if x['v_type'] == 'phone_number':
            userPhone = x['v_id']
        if x['v_type'] == 'email':
            userEmail = x['v_id']
    userCreatedDate = q[0]['S1'][0]['attributes']['created_date']
    return [
        html.Br(),
        html.P(f"User Account Name: {userAccount}", style={'color': 'black'}),
        html.P(f"User Account Email: {userEmail}", style={'color': 'black'}),
        html.P(f"User Account Phone Number: {userPhone}", style={'color': 'black'}),
        html.P(f"User Account Created Date: {userCreatedDate}", style={'color': 'black'}),
    ]


def getUserDates(bank):
    q = conn.runInstalledQuery("getBankAccounts", {'bankName': bank})
    userNums = []
    userDates = []
    count = 1
    for x in q[0]['results']:
        userDates.append(x['attributes']['created_date'])
        userNums.append(count)
        count += 1
    df = pd.DataFrame(list(zip(userNums, userDates)), columns=['count', 'date'])
    fig = px.line(df, x='date', y='count', title='Number of Users')
    fig.update_xaxes(rangeslider_visible=True)
    return dcc.Graph(figure=fig)


# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), navbar, sidebar, content])


# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 6)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False, False
    return [pathname == f"/page-{i}" for i in range(1, 6)]


@app.callback(Output("userIdOutput", "children"), [Input(component_id="userIdSubmit", component_property="n_clicks")], [State("userId", "value")])
def output_text(n_clicks, userID):
    if n_clicks != 0:
        try:
            # df = pd.DataFrame(q[0]['S1'])
            # print(q[0]['S1'][0]['attributes']['created_date'])
            # value = q[0]['S1'][0]['attributes']['created_date']
            # return dash_table.DataTable(
            #     id='table',
            #     columns=[{'name': i, "id": i} for i in df.columns],
            #     data=df.to_dict('records'),
            # )
            # return getUserInfo(userID)
            return getUserDates(userID)
        except Exception as e:
            return [html.Br(), html.P("Please enter Valid Patient ID", style={'color': 'red'})]
    else:
        return


options = ['Get Bank Info', 'Get User Info']
# bank_options = ['Visa', 'Bank of America', 'Mastercard', 'American Express 95']


def getBanks():
    q = conn.runInstalledQuery("getAllBanks", {})
    # print(str(q))
    results = []
    for x in q[0]['seed']:
        results.append(x['v_id'])
    return dcc.Dropdown(
        id='bank-options',
        options=[{'label': i, 'value': i} for i in results],
        searchable=False,
    )

@app.callback(Output('user-input-dropdown', 'children'), [Input('query-options-radio', 'value')])
def set_bank_options(selected_value):
    if selected_value == 'Get Bank Info':
        try:
            return getBanks()
        except Exception as e:
            print('error')
    else:
        return html.P('User')

def getBankTransactions(bank):
    q = conn.runInstalledQuery("getBankTransactions", {'bankID': bank})
    payments = []
    amounts = []
    dates = []
   
    # print(q)
    # print(q[0]['S1'][0]['v_id'])
    for x in q[0]['S1']:
        payments.append(x['v_id'])
        amounts.append(x['attributes']['amount'])
        dates.append(x['attributes']['transaction_date'])

    df = pd.DataFrame(list(zip(payments, amounts, dates)), columns=['id', 'amount', 'date'])

    fig = px.line(df, x='date', y='amount', title='Bank Transactions')

    fig.update_xaxes(rangeslider_visible=True)
    return dcc.Graph(figure=fig)


@app.callback(Output('display-bank-options', 'children'), [Input('bank-options', 'value')])
def set_bank_users(selected_bank):
    try:
        return getBankTransactions(selected_bank)
    except Exception as e:
        return [html.Br(), html.P("Error grabbing graph data", style={'color': 'red'})]

@app.callback(Output('bank-options', 'value'), [Input('bank-options', 'options')])
def set_bank_value(available_options):
    return available_options[0]['value']


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return html.P(page1)
    elif pathname == "/page-2":
        return html.P(page2)
    elif pathname == "/page-3":
        return html.P(conn.gsql('ls'))
    elif pathname == "/page-4":
        return kepler_page
    elif pathname == "/page-5":
        return callbackPage
    elif pathname == "/page-6":
        return graphistry_page

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(port=8881)
