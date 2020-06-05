import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from utils import Header
from app import app
import numpy as np
import pandas as pd

#doing this one because I don't understand what it's doing from the example
np.random.seed(0)
df = pd.DataFrame({"Col " + str(i+1): np.random.rand(30) for i in range(6)})

layout = html.Div([
    html.Div([Header(app)]),
    html.Div(dcc.Graph(id = 'g1', config={'displayModeBar': False}),
             className='four columns'),
    html.Div(dcc.Graph(id = 'g2', config={'displayModeBar': False}),
             className='four columns'),
    html.Div(dcc.Graph(id = 'g3', config={'displayModeBar': False}),
             className='four columns')
],className = 'row')

def get_figure(df, x_col, y_col, selectedpoints,selectedpoints_local):

    if selectedpoints_local and selectedpoints_local['range']:
        ranges = selectedpoints_local['range']
        selection_bounds = {'x0': ranges['x'][0], 'x1': ranges['x'][1],
                            'y0': ranges['y'][0], 'y1': ranges['y'][1]}
    else:
        selection_bounds = {'x0': np.min(df[x_col]), 'x1': np.max(df[x_col]),
                            'y0': np.min(df[y_col]), 'y1': np.max(df[y_col])}
    return {
        'data': [{
            'x': df[x_col],
            'y': df[y_col],
            'text': df.index,
            'textposition': 'top',
            'selectedpoints': selectedpoints,
            'customdata': df.index,
            'type': 'scatter',
            'mode': 'markers+text',
            'marker': { 'color': 'rgba(0, 116, 217, 0.7)', 'size': 12 },
            'unselected': {
                'marker': { 'opacity': 0.3 },
                'textfont': { 'color': 'rgba(0, 0, 0, 0)' }
            }
        }],
        'layout': {
            'margin': {'l': 20, 'r': 0, 'b': 15, 't': 5},
            'dragmode': 'select',
            'hovermode': False,
            'shapes': [dict({
                'type': 'rect',
                'line': { 'width': 1, 'dash': 'dot', 'color': 'darkgrey' }
            }, **selection_bounds
            )]
        }
    }

@app.callback(
    [Output('g1', 'figure'),
     Output('g2', 'figure'),
     Output('g3', 'figure')],
    [Input('g1', 'selectedData'),
     Input('g2', 'selectedData'),
     Input('g3', 'selectedData')]
)
def callback(selection1, selection2, selection3):
    selectedpoints = df.index
    for selected_data in [selection1, selection2, selection3]:
        if selected_data and selected_data['points']:
            selectedpoints = np.intersect1d(selectedpoints,
                [p['customdata'] for p in selected_data['points']])

    return [get_figure(df, "Col 1", "Col 2", selectedpoints, selection1),
            get_figure(df, "Col 3", "Col 4", selectedpoints, selection2),
            get_figure(df, "Col 5", "Col 6", selectedpoints, selection3)]