import plotly.graph_objects as go


class C19Plotly(object):
    def __init__(self, daily_data, gov_dataset):
        self.df = daily_data
        self.df_hspc = gov_dataset
        self.x = self.df['date']
        self.x_hspc = self.df_hspc['Date']

    def get_graph_settings(self, title):
        settings = {
            "title": {'text': title,
                      'y': 0.9,
                      'x': 0.5,
                      'xanchor': 'center',
                      'yanchor': 'top'},
            "xaxis_title": "Time",
            "yaxis_title": "Cases",
            "height": 600,
            "font": dict(
                #family="Courier New, monospace",
                size=16,
                color="#7f7f7f")

        }
        return settings

    def get_icu_vs_vent_fig(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=self.x, y=self.df['c19_icu_cases_rm'], name="Daily C19 ICU Cases (3 Day RM)", mode='lines+markers'))
        fig.add_trace(go.Bar(x=self.x, y=self.df['c19_ventilated_cases'],
                                name="Daily Confirmed c19 Ventilation cases", marker_color='lightgrey'))
        fig.add_trace(go.Scatter(
            x=self.x, y=self.df['c19_ventilated_cases_rm'], name="c19 Ventilation cases (3 Day RM)", mode='lines+markers'))
        fig.add_trace(go.Scatter(
            x=self.x, y=self.df['available_icu_beds_rm'], name="Daily Available ICU Beds (3 Day RM)", mode='lines+markers'))

        fig.update_layout(
            self.get_graph_settings("Daily Ventilation Cases Vs ICU Cases Vs Available ICU Beds")
        )
        return fig

    def get_icu_cases_fig(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=self.x_hspc, y=self.df_hspc['RequiringICUCovidCases_new_rm'], name="Daily New C19 ICU (3 Day RM)", mode='lines+markers'))
        fig.add_trace(go.Bar(x=self.x_hspc, y=self.df_hspc['RequiringICUCovidCases_new'],
                                name="Daily New C19 ICU", marker_color='lightgrey'))

        fig.update_layout(self.get_graph_settings("Daily C19 ICU"))
        return fig

    def get_hos_cases_fig(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=self.x_hspc, y=self.df_hspc['HospitalisedCovidCases_new_rm'], name="Daily C19 Hospitalised (3 Day RM)", mode='lines+markers'))
        fig.add_trace(go.Bar(x=self.x_hspc, y=self.df_hspc['HospitalisedCovidCases_new'],
                                name="Daily C19 Hospitalised", marker_color='lightgrey'))

        fig.update_layout(self.get_graph_settings("Daily C19 Hospitilisation All Ages"))
        return fig

    def get_deaths_fig(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=self.x_hspc, y=self.df_hspc['ConfirmedCovidDeaths_rm'], name="Daily C19 Deaths (3 Day RM)", mode='lines+markers'))
        fig.add_trace(go.Bar(x=self.x_hspc, y=self.df_hspc['ConfirmedCovidDeaths'],
                                name="Daily C19 Deaths", marker_color='lightgrey'))

        fig.update_layout(self.get_graph_settings("Daily C19 Deaths"))
        return fig

    def get_icu_vs_hos_vs_deaths_vs_cases_fig(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=self.x_hspc, y=self.df_hspc['HospitalisedCovidCases_new_rm'], name="Daily C19 Hospitalised (3 Day RM)", mode='lines+markers'))
        fig.add_trace(go.Scatter(
            x=self.x_hspc, y=self.df_hspc['RequiringICUCovidCases_new_rm'], name="Daily New C19 ICU (3 Day RM)", mode='lines+markers'))
        fig.add_trace(go.Scatter(
            x=self.x_hspc, y=self.df_hspc['ConfirmedCovidCases_new_rm'], name="Daily New C19 Cases (3 Day RM)", mode='lines+markers'))
        fig.add_trace(go.Scatter(
            x=self.x_hspc, y=self.df_hspc['ConfirmedCovidDeaths_rm'], name="Daily C19 Deaths (3 Day RM)", mode='lines+markers'))

        fig.update_layout(self.get_graph_settings("Daily Hospitilisation vs ICU vs Cases vs Deaths"))
        return fig
