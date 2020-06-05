import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from os import listdir
folders = [i for i in listdir('./pages') if i not in ['.DS_Store','__pycache__']]


def Header(app):
    return html.Div([html.Br([]), get_menu()])

#now that we need to nest files, we change how page_options is structured
def get_menu():
    menu = html.Div(
        [dbc.DropdownMenu(
            label = folder,
            children = [dbc.DropdownMenuItem(
                name,
                href = "/" + folder + "/"+name,
                className = "tab",
            ) for name in [i.replace('.py','') for i in listdir('./pages/' + folder) if '.py' in i]]
            )
            for folder in folders
            ],
        className = "row all-tabs"
    )
    return menu