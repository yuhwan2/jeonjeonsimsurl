import pandas as pd
import numpy as np
import os as os
import params as pa

def DataReader(Loc, Filename):
    Path = os.path.join(Loc, Filename)
    TempWeather = pd.read_csv(Path)
    TempWeather["DeliveryDT"] = pd.to_datetime(TempWeather["DeliveryDT"], format='%Y-%m-%d %H:%M:%S', utc=False)
    return TempWeather
