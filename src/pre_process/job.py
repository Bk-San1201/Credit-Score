import pandas as pd
from pandas import DataFrame
import csv
import json
import numpy as np

def check_job():
    df = pd.read_csv('./Data/train_input.csv', low_memory=False)
    job = df['maCv'].unique()
    for j in job:
        print(j)
        
if __name__ == "__main__":
    check_job()