import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import flask


app= flask.Flask(__name__)
dash_app = dash.Dash(__name__, server=app, external_stylesheets=[dbc.themes.BOOTSTRAP])
dash_app.config.suppress_callback_exceptions = True

dash_app.layout = html.Div(
    children=[
        html.H1(children="FreeBirds Crew"),
        html.Div(children="""Docker Conatiner Running DASH WebApp"""),
        dcc.Graph(
            id="example-graph",
            figure={
                "data": [
                    {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "Like"},
                    {
                        "x": [1, 2, 3],
                        "y": [2, 4, 5],
                        "type": "bar",
                        "name": "Comment",
                    },
                ],
                "layout": {"title": "Like Vs Comment Dash Visualization"},
            },
        ),
    ]
)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)