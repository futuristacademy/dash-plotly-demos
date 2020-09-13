import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

radioitems = dbc.FormGroup(
    [
        dbc.Label("Choose one"),
        dbc.RadioItems(
            options=[
                {"label": "Option 1", "value": 1},
                {"label": "Option 2", "value": 2},
                {"label": "Disabled option", "value": 3, "disabled": True},
            ],
            value=1,
            id="radioitems-input",
            inline=True,
        ),
    ]
)

checklist = dbc.FormGroup(
    [
        dbc.Label("Choose a bunch"),
        dbc.Checklist(
            options=[
                {"label": "Option 1", "value": 1},
                {"label": "Option 2", "value": 2},
                {"label": "Disabled Option", "value": 3, "disabled": True},
            ],
            value=[],
            id="checklist-input",
            labelCheckedStyle={"color": "red"},
        ),
    ]
)

switches = dbc.FormGroup(
    [
        dbc.Label("Toggle a bunch"),
        dbc.Checklist(
            options=[
                {"label": "Option 1", "value": 1},
                {"label": "Option 2", "value": 2},
                {"label": "Disabled Option", "value": 3, "disabled": True},
            ],
            value=[],
            id="switches-input",
            switch=True,
        ),
    ]
)


app.layout = dbc.Container([
    html.Div(
        [
            dbc.Form([radioitems, checklist, switches]),
            html.P(id="radioitems-checklist-output"),
        ]
    ),

    html.Br(),
    html.Div(
        [
            dbc.FormGroup(
                [
                    dbc.Checkbox(
                        id="standalone-checkbox", className="form-check-input"
                    ),
                    dbc.Label(
                        "This is a checkbox",
                        html_for="standalone-checkbox",
                        className="form-check-label",
                    ),
                ],
                check=True,
            ),
            dbc.FormGroup(
                [
                    dbc.RadioButton(
                        id="standalone-radio", className="form-check-input"
                    ),
                    dbc.Label(
                        "This is a radio button",
                        html_for="standalone-radio",
                        className="form-check-label",
                    ),
                ],
                check=True,
            ),
            html.Br(),
            html.P(id="standalone-radio-check-output"),
        ]
    ),

], className='mt-3')

@app.callback(
    Output("radioitems-checklist-output", "children"),
    [
        Input("radioitems-input", "value"),
        Input("checklist-input", "value"),
        Input("switches-input", "value"),
    ],
)
def on_form_change(radio_items_value, checklist_value, switches_value):
    template = "Radio button {}, {} checklist item{} and {} switch{} selected."

    n_checkboxes = len(checklist_value)
    n_switches = len(switches_value)

    output_string = template.format(
        radio_items_value,
        n_checkboxes,
        "s" if n_checkboxes != 1 else "",
        n_switches,
        "es" if n_switches != 1 else "",
    )
    return output_string


@app.callback(
    Output("standalone-radio-check-output", "children"),
    [
        Input("standalone-checkbox", "checked"),
        Input("standalone-radio", "checked"),
    ],
)
def on_form_change(checkbox_checked, radio_checked):
    if checkbox_checked and radio_checked:
        return "Both checked."
    elif checkbox_checked or radio_checked:
        return "One checked."
    else:
        return "None checked."

if __name__ == '__main__':
    app.run_server(debug=True)