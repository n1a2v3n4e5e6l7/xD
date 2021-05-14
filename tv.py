  
import plotly.express as px
import csv
import numpy as np

def getDataSource(DataPath):
    sizeoftv = []
    averagetime = []
    with open (DataPath) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            sizeoftv.append(float(row["Size of TV"]))
            averagetime.append(float(row["	Average time spent watching TV in a week (hours)"]))   
        return{"x":sizeoftv,"y":averagetime}

def findCo_Relation(DataSource):
    corelation = np.corrcoef(DataSource["x"],DataSource["y"])
    print("Co-Relation Between sizeoftv vs SoftDrink: \n --->",corelation[0,1])

def Main():
    createDataPth = "tv.csv"
    DataSource = getDataSource(createDataPth)
    findCo_Relation(DataSource)

Main()