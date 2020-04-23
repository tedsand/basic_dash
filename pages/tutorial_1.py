import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from utils import Header

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

def generate_table(df,max_rows=10):
	return html.Table([
		html.Thead(
			html.Tr([html.Th(col) for col in df.columns])
		),
		html.Tbody([
			html.Tr([
				html.Td(df.iloc[i][col]) for col in df.columns
			]) for i in range(min(len(df), max_rows))
		])
	])

colors = {
	'background': '#111111',
	'text': '#7FDBFF'
}

def create_layout(app):
	# Page layout
	return html.Div(
		[
			html.Div([Header(app)]),
    	generate_table(df)
		])
