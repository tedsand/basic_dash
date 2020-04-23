import dash_core_components as dcc
import dash_html_components as html
from utils import Header

markdown_text = '''
### Talking 'Bout Markdown

This is marked down. Not full price! 
Here's a [hyperlink](http://youtube.com)
'''
def create_layout(app):
    return html.Div([
        html.Div([Header(app)]),
        dcc.Markdown(children=markdown_text)
    ])