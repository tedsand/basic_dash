import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from utils import Header
from app import app

#write page layout here
layout = html.Div([
    html.Div([Header(app)]),
])