import plotly.express as px
import csv
with open("ice-cream.csv")as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x = "Temperature",y = "Ice-cream Sales")
    fig.show()