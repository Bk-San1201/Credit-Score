import pandas as pd
from pandas import DataFrame
import csv

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
    for c in input_str:
        if c in s1:
            s += s0[s1.index(c)]
        else:
            s += c
    return s.lower()      
    
def make_train_output():
    df = pd.read_csv('./Data/train.csv')
    col = DataFrame(df, columns=['id', 'label'])
    col.to_csv('./Data/train_output.csv', index=False)
    print(col)

def make_train_input():
    df = pd.read_csv('./Data/train.csv')
    df.pop('label')
    df.to_csv('./Data/train_input.csv', index=False)

if __name__ == "__main__":
    format()