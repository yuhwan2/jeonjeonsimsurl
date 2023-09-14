import pandas as pd
import numpy as np
from Forecasting import predictor as pr
import params as pa
import os

if __name__ == '__main__' :
    File = "Solar_4.csv"
    Solar = pr.TargetDataReader(pa.Loc, File)

    print(Solar)

    Saver=[]
    FileList = os.listdir(pa.Loc)
    for f in FileList:
        if f[0]=="0" :
            Data = pr.DataReader(pa.Loc, f)
            Saver.append(Data)

    Weather = pd.concat(Saver, ignore_index=True)
    Weather = Weather.sort_values(by="DeliveryDT", ascending=[True])
    Weather.index = range(0, len(Weather))

    Total = pd.merge(Solar, Weather, how='inner', on="DeliveryDT")

    print(Total)