import plotly.express as px
import csv
import numpy as np
def getdatasource():
    Temperature = []
    icecream = []
    softdrink = []
    with open("ice-cream.csv")as f:
        df = csv.DictReader(f)
        print("i am here")
    for row in df:
      
        Temperature.append(float(row["Temperature"]))
        icecream.append(float(row["Ice-cream Sales"]))
        softdrink.append(float(row["Cold drink sales"]))
    return{"x":Temperature,"y":softdrink}
def findcorelation(datasource):
    corelation = np.corrcoef(datasource["x"],datasource["y"])
    print ("corelation between temperature and soft drink is : ",corelation[0,1])
def main():
    ds = getdatasource()
    findcorelation(ds)
main()
                                                