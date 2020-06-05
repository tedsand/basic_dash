import dash_core_components as dcc
import dash_html_components as html
from utils import Header
from app import app

markdown_text = '''
### Summary of fixing my multi-page dash app.

The first thing I did was a totally hacky attempt at copying the example 
[Dash Financial Report](https://dash-gallery.plotly.host/dash-financial-report/).

This worked well enough (especially once I figured out how to put the CSS in the right place) but broke on callbacks.
The first useful resource I found was 
[this](https://medium.com/@olegkomarov_77860/how-to-embed-a-dash-app-into-an-existing-flask-app-ea05d7a2210b)
blog post talking about related issues which then directed me to the 
[official documentation](https://dash.plotly.com/urls).

The official documentation has a couple of different examples which I'm still assessing to figure out if any of them 
can do what I'm trying to do here. The first example is just a url based callback that doesn't actually build distinct
pages. The second is close to the pattern of the report I copied. It uses a display_page function to toggle between
the different options and has callbacks that work. 

However this doesn't use the same file structure as the initial app uses and that I desire. While the page layouts are 
defined outside of the main app description and thus able to be written in separate files and imported, callbacks are 
still defined in the main file. There is a flag which prevents the callbacks from raising issues under this structure 
but this pattern still doesn't allow the callbacks to be defined in the separate files and all work in the main file.

I *think* the third example is not super relevant to what I'm trying to do but it's definitely possible I'll come back 
and realize it was the answer all along.

The fourth example looks like it's what I have to do. Define app and index as separate files and do a real import of app
into the intermediate pages and then reimport to index. This has working callbacks in separately defined pages, which is 
issue I'm currently having.
'''
layout =  html.Div([
    html.Div([Header(app)]),
    dcc.Markdown(children=markdown_text)
])