import pandas as pd
import numpy as np
import matplotlib as mpl

def getZip(boro):
    df = pd.read_csv("./NYC-vehicle-collisions.csv")
    myBoro = df.loc[(df["BOROUGH"] == boro)]
    deadZip = int(myBoro["ZIP CODE"].value_counts().idxmax())
    return deadZip