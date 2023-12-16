import pandas as pd
import plotly.express as px
from dash import dash, dcc, html, Input, Output
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#  Erstellen der Dash Applikation
app = dash.Dash(__name__)

# Einlesen des Datasets in einen Dataframe
df = pd.read_csv("./Data/original.csv")

# Layout der Dash Applikation für Teilaufgabe b
page1_layout = html.Div([
    html.H1("Logistische Regression")])

@app.callback(
        Output()
)
def calc_logistic_regression():
    #splitting into 90% Training and 10% Test set
    df_train, df_test = train_test_split(df, test_size=0.1, random_state=0, stratify=True)


    #feature scaling
    scaler = StandardScaler()

    scaler.fit_transform()
    scaler.transform()

    classifier = LogisticRegression(random_state=98).fit()

    return 


# Layout der Dash Applikation für Teilaufgabe b
page2_layout = html.Div([
    html.H1("Decision Tree")])

@app.callback(
)
def update_decision_tree():

    return 

# Layout der Dash Applikation für Teilaufgabe b
page3_layout = html.Div([
    html.H1("K-Nearest Neighbor")])

@app.callback(
)
def update_knn():

    return 

# App Layout mit den Tabs
app.layout = html.Div([
    html.H1(children='IVDA Aufgabe 3'),
    dcc.Tabs(id='tabs', value='page1', children=[
        dcc.Tab(label='Logistische Regression', value='page1'),
        dcc.Tab(label='Decision Tree', value='page2'),
        dcc.Tab(label='K-Nearest Neighbor', value='page3')
    ]),
    html.Div(id='page-content')
])


# Callback und Funktion um über die Tabbar die einzelnen Seiten-
# layout aufzurufen


@app.callback(Output('page-content', 'children'), [Input('tabs', 'value')])
def display_page(tab):
    if tab == 'page1':
        return page1_layout
    elif tab == 'page2':
        return page2_layout
    elif tab == 'page3':
        return page3_layout


# Starten der Dash Applikation


if __name__ == '__main__':
    app.run_server(debug=True)