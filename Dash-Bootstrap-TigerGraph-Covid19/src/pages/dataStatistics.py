import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
# import connect
import plotly.graph_objects as go

# conn = connect.getConnection()
vertex_x_axis = []
vertex_y_axis = []
edge_x_axis = []
edge_y_axis = []
percentage_x = []


def getData(conn):
    fig = None
    fig2 = None
    fig3 = None
    try:
        vertexData = conn.getVertexCount(vertexType="*")
        edgeData = conn.getEdgeCount(edgeType="*")

        for x in vertexData.keys():
            vertex_x_axis.append(x)
            vertex_y_axis.append(vertexData[x])
        for y in edgeData.keys():
            edge_x_axis.append(y)
            edge_y_axis.append(edgeData[y])

        sorted_vertex_labels = [x for _, x in sorted(zip(vertex_y_axis, vertex_x_axis), reverse=True)]
        sorted_vertex_values = sorted(vertex_y_axis, reverse=True)
        sorted_edge_labels = [x for _, x in sorted(zip(edge_y_axis, edge_x_axis), reverse=True)]
        sorted_edge_values = sorted(edge_y_axis, reverse=True)

        percentage_x.append(sorted_vertex_values)
        percentage_x.append(sorted_edge_values)

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=sorted_vertex_labels,
            y=sorted_vertex_values,
            name='Vertices',
            marker_color='rgba(239, 108, 0, 0.7)'
        ))
        fig.add_trace(go.Bar(
            x=sorted_edge_labels,
            y=sorted_edge_values,
            name='Edges',
            marker_color='rgba(66, 66, 66, 0.7)'
        ))
        fig.update_layout(
            title='Vertex and Edge Count',
            yaxis=dict(
                title='Count',
                type='log'
            ),
            xaxis=dict(
                title='Name'
            ),
            height=500,
        )
        total_vertex = sum(percentage_x[0])
        total_edge = sum(percentage_x[1])
        for i in range(len(percentage_x[0])):
            percentage_x[0][i] = percentage_x[0][i] / total_vertex
        for i in range(len(percentage_x[1])):
            percentage_x[1][i] = percentage_x[1][i] / total_edge
        # fig2.add_trace(go.Bar(
        #     x=percentage_x[0], y=percentage_y,
        #     orientation='h',
        #     marker=dict(
        #         color='rgba(38, 24, 74, 0.8)',
        #         line=dict(color='rgb(248, 248, 249)', width=1)
        #     )
        # ))
        # fig2.add_trace(go.Bar(
        #     x=percentage_x[1], y=percentage_y,
        #     orientation='h',
        #     marker=dict(
        #         color='rgba(38, 24, 74, 0.8)',
        #         line=dict(color='rgb(248, 248, 249)', width=1)
        #     )
        # ))
        percentage_y = [['Vertices'] * len(percentage_x[0]), ['Edges'] * len(percentage_x[1])]
        fig2 = go.Figure(go.Bar(
            x=percentage_x[0], y=percentage_y[0],
            orientation='h',
            hovertext=sorted_vertex_labels,
            # marker_color='rgba(239, 108, 0, 0.7)'
            marker_color=[f'rgba({239+20*i}, {108+20*i}, {0+20*i}, {0.7})' for i in range(len(percentage_x[0]))]
        ))
        fig2.update_layout(
            xaxis=dict(
                tickformat=',.0%',
                range=[0, 1]
            ),
            margin=dict(
                t=0
            ),
            height=150,
        )
        fig3 = go.Figure(go.Bar(
            x=percentage_x[1], y=percentage_y[1],
            orientation='h',
            hovertext=sorted_edge_labels,
            marker_color=[f'rgba({66+20*i}, {66+20*i}, {66+20*i}, {0.7})' for i in range(len(percentage_x[1]))]
        ))
        fig3.update_layout(
            xaxis=dict(
                tickformat=',.0%',
                range=[0, 1]
            ),
            margin=dict(
                t=0
            ),
            height=150,
        )
    except Exception as e:
        print('error: ', e)
    return fig, fig2, fig3, total_vertex, total_edge




def get_page(conn):

    fig, fig2, fig3, total_vertex, total_edge = getData(conn)


    page = html.Div(
        [
            html.H2("Graph Statistics"),
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            [
                                # html.Br(),
                                html.H3(f'{total_vertex}'),
                                html.H6('Vertex'),
                            ],
                            style={'text-align': 'center', 'vertical-align': 'middle', 'height': '125px', 'padding-top': '0%'}
                        ),
                        width=2,
                    ),
                    dbc.Col(
                        html.Div(
                            dcc.Graph(figure=fig2),
                        ),
                        width=10,
                    ),
                ],
                style={'margin-bottom': '10px', 'width': '100%', 'height': '125px'}
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            [

                                # html.Br(),
                                html.H3(f'{total_edge}'),
                                html.H6('Edge'),
                            ],
                            style={'text-align': 'center', 'vertical-align': 'middle', 'height': '125px', 'padding-top': '0%'}
                        ),
                        width=2,
                    ),
                    dbc.Col(
                        html.Div(
                            dcc.Graph(figure=fig3),
                        ),
                        width=10,
                    ),
                ],
                style={'margin-bottom': '10px', 'width': '100%', 'height': '125px'}
            ),
            html.Div(
                dcc.Graph(figure=fig),
            )
        ]
    )
    return page
