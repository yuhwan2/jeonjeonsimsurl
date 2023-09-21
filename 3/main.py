import numpy as np

from Forecasting import predictor as pr
import params as pa
import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


pd.set_option('display.width', 5000)
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Target
    File = "RenewableHist.csv"
    Solar = pr.DataReader(pa.Loc, File)
    Solar = Solar.sort_values(by=['DeliveryDT'], ascending=[True])

    # Weather
    FileList = os.listdir(pa.Loc)
    Saver=[]
    for f in FileList:
        if f[0:11] == "WeatherHist":
            Data = pr.DataReader(pa.Loc, f)
            Saver.append(Data)

    Weather = pd.concat(Saver,ignore_index=True)
    Weather = Weather.sort_values(by=["DeliveryDT"], ascending=[True])
    Weather.index = range(0, len(Weather))

    del Weather['#']
    del Weather['WeatherHistId']

    Col = ['pres','slp','wind_spd','wind_dir','temp','app_temp','rh,dewpt','clouds','vis','precip','snow','uv,solar_rad','vapor','snow_depth']
    Unique = Weather['WeatherStationId'].unique()

    for i in range(0, len(Unique)) :
        Temp = Weather[Weather['WeatherStationId'] == Unique[i]]
        del Temp['WeatherStationId']
        for cc in Col:
            Temp = Temp.rename(columns = {cc: cc+ '_' + str(Unique[i])})
        if i == 0:
            Saver = Temp.copy()
        else:
            Saver=pd.merge(Saver,Temp,how='inner', on='DeliveryDT')


    Total = pd.merge(Solar,Saver,how='inner', on="DeliveryDT")
    Total = Total.sort_values(by=['DeliveryDT'], ascending=[True])
    Total.index = range(0, len(Total))
    Total = Total.fillna(-9999)
    Total = Total.loc[60000 : 63528,]


    machine = RandomForestRegressor(
        n_estimators = 100,
        criterion = 'squared_error',
        max_depth = 30,
        verbose = 1)

    Y_train=Total['MW']
    X_train=Total.copy()
    del X_train['MW']
    del X_train['DeliveryDate']
    del X_train['DeliveryDT']

    machine.fit(X_train, Y_train)
    importances = machine.feature_importances_
    pred = machine.predict(X_train)
    pred = np.round(pred, 2)

    SE = np.abs(Y_train - pred) *np.abs(Y_train - pred)
    MSE = np.mean(SE)
    RMSE = np.sqrt(MSE)

    plt.figure(1)
    plt.plot(range(0, len(Y_train)), Y_train, label = 'Actual')
    plt.plot(range(0, len(Y_train)), pred, label = 'prediction')
    plt.legend()
    plt.title(RMSE)
    plt.grid(True)
    plt.draw()
    plt.show(block = False)

    x_train, x_test, y_train, y_test = train_test_split(X_train, Y_train, shuffle = False, test_size = 0.1, random_state = 0)

    machine.fit(x_train, y_train)
    importances = machine.feature_importances_
    pred = machine.predict(x_test)
    pred = np.round(pred, 2)

    SE = np.abs(y_test - pred) * np.abs(y_test - pred)
    MSE = np.mean(SE)
    RMSE = np.sqrt(MSE)

    plt.figure(2)
    plt.plot(range(0, len(y_test)), y_test, label='Actual')
    plt.plot(range(0, len(y_test)), pred, label='prediction')
    plt.legend()
    plt.title(RMSE)
    plt.grid(True)
    plt.draw()
    plt.show(block=False)



    ########

    print(Total)




