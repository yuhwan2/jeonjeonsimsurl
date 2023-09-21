from Forecasting import predictor as pr
import params as pa
import pandas as pd
import os

pd.set_option('display.width', 5000)
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Target
    File = "Solar_4.csv"
    Solar = pr.DataReader(pa.Loc, File)

    # Weater
    FileList = os.listdir(pa.Loc)
    Saver=[]
    for f in FileList:
        if f[0] == "W":
            Data = pr.DataReader(pa.Loc, f)
            Saver.append(Data)

    Weather=pd.concat(Saver,ignore_index=True)
    Weather = Weather.sort_values(by=["DeliveryDT"], ascending=[True])
    Weather.index = range(0, len(Weather))

    Total=pd.merge(Solar,Weather,how='inner', on="DeliveryDT")

    ########

    print(Total)




