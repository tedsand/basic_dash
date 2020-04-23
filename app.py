
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import importlib
from os import listdir

page_options = [i.replace('.py','') for i in listdir("./pages") if '.py' in i]
page_dict = {i:importlib.import_module("pages." + i) for i in page_options}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
						'https://github.com/tedsand/basic_dash/blob/master/basic.css']

app = dash.Dash(__name__,external_stylesheets = external_stylesheets)

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
		return page_dict["tutorial_1"].create_layout(app)
	elif pathname.replace("/","") in page_dict:
		return page_dict[pathname.replace("/","")].create_layout(app)
	else:
		return page_dict["tutorial_1"].create_layout(app)

if __name__ == '__main__':
	app.run_server(debug=True)
