# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px

from src.ireland_c19_data import get_daily_c19_ireland_data, get_gov_c19_ireland_dataset

df = get_daily_c19_ireland_data()
df_hspc = get_gov_c19_ireland_dataset()
x = df['date']
x_hspc = df_hspc['Date']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


def get_icu_vs_vent_fig():
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=df['c19_icu_cases_rm'], name="Daily C19 ICU Cases (3 Day RM)"))
    fig.add_trace(go.Bar(x=x, y=df['c19_ventilated_cases'],
                         name="Daily Confirmed c19 Ventilation cases"))
    fig.add_trace(go.Scatter(
        x=x, y=df['c19_ventilated_cases_rm'], name="c19 Ventilation cases (3 Day RM)"))
    fig.add_trace(go.Scatter(
        x=x, y=df['available_icu_beds_rm'], name="Daily Available ICU Beds (3 Day RM)"))

    fig.update_layout(
        title={'text':"Daily Ventilation Cases Vs ICU Cases Vs Available ICU Beds",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title="Time",
        yaxis_title="Cases",
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="#7f7f7f"
        )
    )
    return fig

def get_icu_cases_fig():
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x_hspc, y=df_hspc['RequiringICUCovidCases_new_rm'], name="Daily New C19 ICU (3 Day RM)"))
    fig.add_trace(go.Bar(x=x_hspc, y=df_hspc['RequiringICUCovidCases_new'],
                         name="Daily New C19 ICU"))

    fig.update_layout(
        title={'text':"Daily C19 ICU",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title="Cases",
        yaxis_title="Time",
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="#7f7f7f"
        )
    )
    return fig


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(children=[
    html.H1(children='Ireland Covid19 Analysis'),

    html.Div(children='''
        Data sources HSPC and Daily Reports.
    '''),

    dcc.Graph(
        id='vent-icu-bed-graph',
        figure=get_icu_vs_vent_fig()
    ),

    dcc.Graph(
        id='icu-graph',
        figure=get_icu_cases_fig()
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
