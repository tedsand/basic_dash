import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from utils import Header
from app import app

layout = html.Div([
    html.Div([Header(app)]),
    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div')
    ])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)