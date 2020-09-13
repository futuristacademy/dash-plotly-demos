import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output, State
import graphistry  as graphistry
import pandas as pd
import plotly.figure_factory as ff
from datetime import timedelta,datetime
import time
import threading
from config import graphistry_pw , graphistry_un


graphistry.register(api=3, protocol="https", server="hub.graphistry.com", username=graphistry_un, password=graphistry_pw)


def type_to_color(t):
    mapper = {'Patient': 0xFF000000}
    if t in mapper:
        return mapper[t]
    else:
        return 0xFFFFFF00

def plotter_thread(df2):
    g = graphistry.edges(df2).bind(edge_color='my_color', source='Source', destination='Destination')
    g = g.settings(url_params={'bg': '%23FFFFFF'})
    graph = g.plot(render=False,name="Zargonovski")
    print("Thread Plotted {}".format(graph)) 
   
    
    
def generateGraph(conn,graphistry_un,graphistry_pw):
    
    try:
        source_col =[]
        source_type =[]
        dest_col =[]
        dest_type =[]
        q = conn.runInstalledQuery("getGraph")
        edges = q[0]['@@AllE']
        # nodes = q[0]['AllV']
        for edge in edges:
            source_col.append(edge['from_id'])
            source_type.append(edge['from_type'])
            dest_col.append(edge['to_id'])
            dest_type.append(edge['to_type'])
        
        
        df = pd.DataFrame(list(zip(source_col, source_type, dest_col, dest_type)), columns=['Source', 'Source_Type', 'Destination', 'Destination_Type'])
        df2 = df.assign(my_color=df['Source_Type'].apply(lambda v: type_to_color(v)))
        
        
        plotting = threading.Thread(target=plotter_thread, args=[(df2)])
        plotting.start()
        from pathlib import Path
        import os
        home = str(Path.home())
        path = '{}/dataset_temp.txt'.format(home)
        while not(os.path.exists(path)):
            time.sleep(1)
        f = open(path)
        dtt = f.read()
        os.remove(path)
        print(dtt)
        graph_viz = html.Iframe(src='https://hub.graphistry.com/graph/graph.html?dataset={}&type=arrow&usertag=e0240123-pygraphistry-0.12.0&info=true&bg=%23FFFFFF'.format(dtt), height='600', width='100%')
        return graph_viz
    except Exception as e:
        print(e)
        time.sleep(10)
        return html.P('There was an error. Double check your username and password in your config file')





def get_page(conn,graphistry_un,graphistry_pw):
    graph = generateGraph(conn,graphistry_un,graphistry_pw)
    # fig = ff.create_table(table)

    page = html.Div(
        [
            html.H2("Graphistry Visualization"),
            graph
        ],
        # style={'height': '100vh'}
    )
    return page
