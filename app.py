# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from src.ireland_c19_data import get_daily_c19_ireland_data, get_gov_c19_ireland_dataset, get_c19_ireland_testing_dataset
from src.c19_plotly import C19Plotly

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

df = get_daily_c19_ireland_data()
df_hspc = get_gov_c19_ireland_dataset()
df_tests = get_c19_ireland_testing_dataset()
c19plotly = C19Plotly(df, df_hspc, df_tests)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

def serve_layout():
    return html.Div(children=[
    dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Ireland Covid19 Analysis", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
        ],
        color="dark",
        dark=True,
    ),

    dcc.Graph(
        id='icu-graph',
        figure=c19plotly.get_icu_cases_fig()
    ),

    dcc.Graph(
        id='hos-graph',
        figure=c19plotly.get_hos_cases_fig()
    ),

    dcc.Graph(
        id='hos-5-14-graph',
        figure=c19plotly.get_hos_cases_5_14_fig()
    ),

    dcc.Graph(
        id='death-graph',
        figure=c19plotly.get_deaths_fig()
    ),

    dcc.Graph(
        id='icu-hos-deaths-graph-40',
        figure=c19plotly.get_icu_vs_hos_vs_deaths_vs_cases_fig_last_40()
    ),

    dcc.Graph(
        id='icu-hos-deaths-graph',
        figure=c19plotly.get_icu_vs_hos_vs_deaths_vs_cases_fig()
    ),

    dcc.Graph(
        id='daily-tests-graph',
        figure=c19plotly.get_daily_tests_fig()
    ),

    dcc.Graph(
        id='vent-icu-bed-graph',
        figure=c19plotly.get_icu_vs_vent_fig()
    )
    
])

app.layout = serve_layout() 
app.title = "Ireland C19 Analysis"


if __name__ == '__main__':
    app.run_server(debug=True)
