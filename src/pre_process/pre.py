import pandas as pd
from pandas import DataFrame
import csv
import json
import numpy as np
def format():   
    with open('./Data/quan_huyen.txt', encoding='utf8') as file:
        prvs = file.read().splitlines()
        new_prvs = []
        for prv in prvs:
            new_prvs.append(remove_accents(prv))
        df = DataFrame(new_prvs, columns=['tinh'])
        df.to_csv('./Data/huyen.csv', index=True)


def check_province():
    df = pd.read_csv('./Data/test.csv')
    col = df['province'].values.tolist()
    set_prvs = set(col)
    with open('./Data/province.txt', encoding='utf8') as file:
        prvs = file.read().splitlines()
        
        for prv1 in set_prvs:
            if prvs.count(prv1) == 0:
                print(prv1)
            
def remove_accents(input_str):
    s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
    s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
    s = ''
    # print(input_str.encode('utf-8'))
    try:
        for c in input_str:
            if c in s1:
                s += s0[s1.index(c)]
            else:
                s += c
        return s.lower()
    except:
        return None

         
    
def make_train_output():
    df = pd.read_csv('./Data/train.csv')
    col = DataFrame(df, columns=['id', 'label'])
    col.to_csv('./Data/train_output.csv', index=False)
    print(col)

def make_train_input():
    df = pd.read_csv('./Data/train.csv')
    # df.pop('label')
    # df.to_csv('./Data/train_input.csv', index=False)

    ar = []
    prvs = df['province'].values.tolist()
    for prv in prvs:
        # print(prv)
        ar.append(remove_accents(prv))
    npAr = np.array(ar)
    df['tinh'] = npAr
    df.to_csv('./Data/train_input.csv', index=False)

    ar1 = []
    prvs = df['district'].values.tolist()
    for prv in prvs:
        # print(prv)
        ar1.append(remove_accents(prv))
    npAr = np.array(ar1)
    print(len(npAr))
    df['huyen'] = npAr
    df.to_csv('./Data/train_input.csv', index=False)



def check_field_7():
    df = pd.read_csv('./Data/train.csv')
    col = DataFrame(df, columns = ['FIELD_7']).values.tolist()
    for row in col:
        # res = json.loads(row)
        # print(res)
        print(row)

def test():
    df = pd.read_csv('./Data/train_input.csv', low_memory=False)
    df_huyen = pd.read_csv('./Data/huyen.csv', low_memory=False)

    listDis = df_huyen['huyen'].values.tolist()
    tmp = df['huyen'].unique()
    i = 0
    for dis in tmp:
        if listDis.count(dis) == 0:
            print(dis)
            i += 1
    print(i / len(tmp))
if __name__ == "__main__":
    test()