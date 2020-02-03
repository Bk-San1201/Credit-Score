import pandas as pd
from pandas import DataFrame
import csv
import json
import numpy as np
import address
import math
from ast import literal_eval

def string2list(string):
    return literal_eval(string)

def check_field_7():
    df = pd.read_csv('./Data/train_input.csv', low_memory=False)
    df1 = pd.read_csv('./Data/test.csv', low_memory=False)
    lst = df['FIELD_7'].values.tolist()
    lst1 = df1['FIELD_7'].values.tolist()
    f = open("./Data/test.txt", 'w', encoding='utf8')
    s = set()
    for i in lst:
        if type(i) is str:
            lst = string2list(i)
            for j in lst:
                s.add(j)
    for i in lst1:
        if type(i) is str:
            lst = string2list(i)
            for j in lst:
                s.add(j)
    for i in s:
        f.write(i)
        f.write('\n')
    f.close()
    s = list(s)
    df_new = DataFrame(s, columns=['FIELD_7'])
    df_new.to_csv('./Data/field_7.csv', index=True)

def check_field(name_field):
    df = pd.read_csv('./Data/train_input.csv', low_memory=False)
    df1 = pd.read_csv('./Data/test.csv', low_memory=False)
    lst = df[name_field].values.tolist()
    lst1 = df1[name_field].values.tolist()
    f = open("./Data/test.txt", 'w', encoding='utf8')
    s = set()
    for i in lst:
        if type(i) is str:
            s.add(i)
    for i in lst1:
        if type(i) is str:
            s.add(i)
    for i in s:
        f.write(i)
        f.write('\n')
    f.close()
    s = list(s)
    df_new = DataFrame(s, columns=[name_field])
    df_new.to_csv('./Data/' + name_field.lower() + '.csv', index=True) 


if __name__ == "__main__":
    check_field('FIELD_9')
    check_field('FIELD_10')
    check_field('FIELD_13')
    check_field('FIELD_17')
    check_field('FIELD_24')
    check_field('FIELD_39')
    check_field('FIELD_41')

    