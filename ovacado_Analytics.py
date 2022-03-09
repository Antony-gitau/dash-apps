#import the libraries we need to create a dash app
from dash import Dash, dcc, html, Input, Output
import pandas as pd #pandas will help in loading data

#load the data
data = pd.read_csv("C:/Users/hp/Downloads/archive (2)/avocado.csv")

#select the data we want-that is rows with region Albany and type conventional
data = data.query("type == 'conventional' and region == 'Albany'")

#format the date column into year, month and date
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")

#sort the columns with date as the reference
data.sort_values("Date", inplace=True)

#start the app, similiar to flask
app = Dash(__name__)

#outline how the app will look like on the web
app.layout = html.Div(
    children=[
        html.H1("Avocado analytics"), #main header
        html.P("Behaviour of ova prices vs ova sold 2015-2018"),

#create a line graph with date on x axis and average price as y axis
        dcc.Graph(
            figure={
                "data":[{
                    "x":data['Date'],
                    "y":data['AveragePrice'],
                    "type":"lines",
                }],
                "layout":{"title": "avg prices of ova"},
            }
        ),

        #create another line graph that will plot date on x axis and sale volume on y axis
        dcc.Graph(
            figure={
                "data":[{
                    "x":data['Date'],
                    "y":data['Total Volume'],
                    "type":"lines",
                }],
                "layout":{"title":"ova sold"}
        })

    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)# Allow hot reloading
