
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import importlib
from os import listdir
from app import app

folders = [i for i in listdir('./pages') if i not in ['.DS_Store','__pycache__']]
page_options = {f:[i.replace('.py','') for i in listdir("./pages/"+ f) if '.py' in i] for f in folders}
page_dict = {}
for folder in page_options:
	for page in page_options[folder]:
		page_dict['/'.join(['',folder,page])] = importlib.import_module('.'.join(['pages',folder,page]))

colors = {
	'background': '#111111',
	'text': '#7FDBFF'
}

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

@app.callback(Output("page-content","children"), [Input("url","pathname")])
def display_page(pathname):
	#if there's a file whose name we recognize in the path, create that page
	if not pathname:
		return page_dict["/tutorial/tutorial_1"].layout
	elif pathname in page_dict:
		return page_dict[pathname].layout
	else:
		return page_dict["/tutorial/tutorial_1"].layout

if __name__ == '__main__':
	app.run_server(debug=True)
