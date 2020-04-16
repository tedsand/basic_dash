import dash_html_components as html
import dash_core_components as dcc
from os import listdir
page_options = [i.replace('.py','') for i in listdir("./pages") if '.py' in i]

def Header(app):
    return html.Div([html.Br([]), get_menu()])


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                name,
                href = "/"+name,
                className = "tab",
            )
            for name in page_options
        ],
        className = "row all-tabs"
    )
    return menu