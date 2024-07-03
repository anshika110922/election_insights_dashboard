from flask import Flask
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

app = Flask(__name__)
dash_app = Dash(__name__, server=app, url_base_pathname='/', external_stylesheets=[dbc.themes.BOOTSTRAP])

# Read CSV files
Electoral165 = pd.read_csv("C://Users//shiva//OneDrive//Desktop//AppBihar//Electoral165.csv")
Electoral166 = pd.read_csv("C://Users//shiva//OneDrive//Desktop//AppBihar//Electoral_166.csv")
Electoral168 = pd.read_csv("C://Users//shiva//OneDrive//Desktop//AppBihar//Electoral_168.csv")
Electoral178 = pd.read_csv("C://Users//shiva//OneDrive//Desktop//AppBihar//Electoral_178.csv")
Electoral179 = pd.read_csv("C://Users//shiva//OneDrive//Desktop//AppBihar//Electoral179.csv")
Electoral167 = pd.read_csv("C://Users//shiva//OneDrive//Desktop//AppBihar//surjgrah.csv")
Candidatedata = pd.read_csv("C://Users//shiva//OneDrive//Desktop//AppBihar//Candidatedata.csv")
Assemblywise = pd.read_csv("C://Users//shiva//OneDrive//Desktop//AppBihar//PC28.csv")
BoothWise165 = pd.read_csv("C://Users//shiva//OneDrive//Desktop//AppBihar//pollingBoothwiseResult165.csv")
BoothWiseResult165 = BoothWise165.iloc[:, [0, 2, 3, 23, 25]]
Expense = pd.read_csv("C://Users//shiva//OneDrive//Desktop//AppBihar//Expenditure_Analysis.csv")
constituencywise = Expense.iloc[:, :4]

# Layout
dash_app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("Overall Voter Turnout Percent"),
            html.H2("57.33%")
        ])), width=4),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("Total Constituency"),
            html.H2("40")
        ])), width=4),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("Total Assembly Seats"),
            html.H2("243")
        ])), width=4)
    ]),
    dbc.Tabs([
        dbc.Tab(label="Dashboard", tab_id="dashboard"),
        dbc.Tab(label="Demographics", tab_id="demographics"),
        dbc.Tab(label="Polling-Booth wise", tab_id="PollingBooth"),
        dbc.Tab(label="Assembly wise", tab_id="assemblies"),
        dbc.Tab(label="Constituency", tab_id="mpconstituency"),
        dbc.Tab(label="Candidate", tab_id="Candidates"),
        dbc.Tab(label="Election Expenditure", tab_id="Expenditure")
    ], id="tabs", active_tab="dashboard"),
    html.Div(id="tab-content")
])

@dash_app.callback(Output("tab-content", "children"), [Input("tabs", "active_tab")])
def render_tab_content(active_tab):
    if active_tab == "dashboard":
        return dbc.Container([
            dbc.Row([
                dbc.Col(dcc.Graph(id="histogram1", figure=px.histogram(Electoral165, x='Age', title='Munger Age distribution')), width=6),
                dbc.Col(dcc.Graph(id="histogram2", figure=px.histogram(Electoral166, x='Age', title='Jamalpur Age distribution')), width=6)
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(id="histogram3", figure=px.histogram(Electoral167, x='Age', title='Surajgraha Age distribution')), width=6),
                dbc.Col(dcc.Graph(id="histogram4", figure=px.histogram(Electoral168, x='Age', title='Lakhisarai Age distribution')), width=6)
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(id="histogram5", figure=px.histogram(Electoral178, x='Age', title='Mokama Age distribution')), width=6),
                dbc.Col(dcc.Graph(id="histogram6", figure=px.histogram(Electoral179, x='Age', title='Badh Age distribution')), width=6)
            ])
        ])
    elif active_tab == "demographics":
        return dbc.Container([
            dbc.Row([
                dbc.Col(dbc.Card(dbc.CardBody([
                    html.H4("Winner"),
                    html.H2("Rajiv Ranjan Singh (Lalan Singh), JD(U)")
                ])), width=7),
                dbc.Col(dbc.Card(dbc.CardBody([
                    html.H4("Runner Up"),
                    html.H2("Nilam Devi, INC")
                ])), width=5)
            ]),
            dbc.Row([
                dbc.Col(html.Img(src="/static/munger.png", height="400px", width="400px")),
                dbc.Col(html.Img(src="/static/mokama.png", height="400px", width="400px"))
            ]),
            dbc.Row([
                dbc.Col(html.Img(src="/static/jamalpur.png", height="400px", width="400px")),
                dbc.Col(html.Img(src="/static/lakhisarai.png", height="400px", width="400px"))
            ]),
            dbc.Row([
                dbc.Col(html.Img(src="/static/badh.png", height="400px", width="400px"))
            ])
        ])
    elif active_tab == "mpconstituency":
        return dbc.Container([
            html.H2("Constituency Wise Voter Turnouts, Winner and Their Winning Margins"),
            dbc.Button("Download", id="consd"),
            dcc.DataTable(id="cons", data=constituencywise.to_dict('records'))
        ])
    elif active_tab == "Expenditure":
        return dbc.Container([
            html.H2("Constituency Wise Election Expenditure by the Winner and Runner-up"),
            dbc.Button("Download", id="expend"),
            dcc.DataTable(id="expen", data=Expense.to_dict('records'))
        ])
    elif active_tab == "assemblies":
        return dbc.Container([
            html.H2("Assembly Wise Results for PC28"),
            dbc.Button("Download", id="assemd"),
            dcc.DataTable(id="assem", data=Assemblywise.to_dict('records'))
        ])
    elif active_tab == "PollingBooth":
        return dbc.Container([
            html.H2("Polling Booth Wise Data"),
            dbc.Button("Download", id="poolingd"),
            dcc.DataTable(id="pooling", data=BoothWiseResult165.to_dict('records'))
        ])
    elif active_tab == "Candidates":
        return dbc.Container([
            html.H2("Candidates Data of the Constituency"),
            dbc.Button("Download", id="candidatetabled"),
            dcc.DataTable(id="candidatetable", data=Candidatedata.to_dict('records'))
        ])
    return html.Div("404 - Page not found")

if __name__ == "__main__":
    app.run(debug=True)
