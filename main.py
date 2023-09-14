import pandas as pd
import numpy as np
from Forecasting import predictor as pr
import params as pa

if __name__ == '__main__' :
    File = "Solar_4.csv"
    Solar = pr.TargetDataReader(pa.loc, File)

    dd