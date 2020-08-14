# dash-plotly-demos

## Getting Started

### Install Dash

1. Run `pip install dash`

[*Dash Docs for More Help*](https://dash.plotly.com/installation)

Note: For HTML with dash use [**Dash HTML Components**](https://dash.plotly.com/dash-html-components)

### Bootstrap Theme for Dash

1. Run `pip install dash-bootstrap-components`
2. Create `index.py`
3. Add the following: 

```
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
``` 



### Resources:

* [Dash-Plotly Website](https://plotly.com/dash/)
* [Dash Bootstrap](https://dash-bootstrap-components.opensource.faculty.ai/)
* [Dash Boostrap GitHub](https://github.com/facultyai/dash-bootstrap-components)
* [Dash Bootsrap Themes](https://bootswatch.com/lux/)

