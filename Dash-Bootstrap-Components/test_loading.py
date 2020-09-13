import time

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

print('App is starting..')

app.layout = html.Div([
    html.Div(id='dynamic-button-container', 
    	children=[
    	html.Button(
    		#id={'type': 'dynamic-button', 'index': 0 },
    		id = 'button0',
    		children= 'Button'
    		)
    	]),
])

@app.callback(
    Output('dynamic-button-container', 'children'),
    [#Input({'type': 'dynamic-button', 'index': ALL}, 'n_clicks')
    Input('button0', 'n_clicks')
    ],
    [State('dynamic-button-container', 'children')])
def display_newbutton(n_clicks, children):
	#if n_clicks[0] is None: return children 
	if n_clicks is None: return children 
	else:
		print('Doing some calculation..') 
		time.sleep(3)

		new_element = html.Button(
		        #id={'type': 'dynamic-button','index': 0 }, #n_clicks[0] },
		        id = 'button0', 
		        children = 'Button' 
		    	)

		children.pop()
		children.append(new_element)
		print('Generating a new button')
		return children

# @app.callback(
#     Output({'type': 'dynamic-button', 'index': 0}, 'disabled'),
#     [Input({'type': 'dynamic-button', 'index': 0}, 'n_clicks')]
# )
@app.callback(
    Output('button0', 'disabled'),
    [Input('button0', 'n_clicks')]
)
def hide_newbutton(n_clicks):
    if n_clicks is None: 
        return False
    else:
        print('Disabling the button')
        return True



if __name__ == '__main__':
    app.run_server(debug=True)