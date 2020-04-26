import dash
#we set up a basic app for other files to import
app = dash.Dash(__name__)
server = app.server
#since the app needs to have callbacks in different page layouts, we suppress exceptions
app.config.suppress_callback_exceptions = True
