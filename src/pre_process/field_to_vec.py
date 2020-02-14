import pandas as pd
from pandas import DataFrame
import csv
import json
import numpy as np
import address
import math
from ast import literal_eval

def format():   
    with open('./Data/quan_huyen.txt', encoding='utf8') as file:
        prvs = file.read().splitlines()
        new_prvs = []
        for prv in prvs:
            new_prvs.append(remove_accents(prv))
        df = DataFrame(new_prvs, columns=['tinh'])
        df.to_csv('./Data/huyen.csv', index=True)

            
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


# Field 7
def string2list(string):
    if type(string) is str:
        return literal_eval(string)
    else:
        return []
    
def encode(strPath):
    # province
    # col = 0 to 64
    # col = 0 means not found
    # col = 1 means Null
    path = '../../'
    df = pd.read_csv(path + strPath, low_memory=False)

    prvs = df['province'].values.tolist()
    vecs = np.ndarray(shape=(len(prvs), 65), dtype=int)
    # print(vecs)
    tinh_formated = pd.read_csv(path + './Data/tinh.csv', low_memory=False)
    tinh_formated = tinh_formated['tinh'].values.tolist()
    print(tinh_formated)

    #-----------------------------------------#
    cnt = 0
    for prv in prvs:
        tmp = np.zeros(65)
        tinh = remove_accents(prv)
        
        if tinh == None:
            tmp[1] = 1
        else:
            dem = 2
            check = True
            for i in tinh_formated:
                if i in tinh:
                    tmp[dem] = 1
                    print(i)
                    check = False
                    break
                else:
                    dem += 1
            if check == True:
                tmp[0] = 1
        vecs[cnt] = tmp
        cnt += 1
    print(vecs)
    #________________________________________________#

    # district (total 711 districts)
    # col 0 to 713
    # col 0 means not found
    # col 1 means null
    df = pd.read_csv(path + strPath, low_memory=False)

    dists = df['district'].values.tolist()
    vecs_district = np.ndarray(shape=(len(dists), 713), dtype=int)

    # print(vecs)
    huyen_formated = pd.read_csv(path + './Data/huyen.csv', low_memory=False)
    huyen_formated = huyen_formated['huyen'].values.tolist()
    print(len(huyen_formated))
    #----------------------------------------------#
    cnt = 0
    for dist in dists:
        tmp = np.zeros(713)
        huyen = remove_accents(dist)
        
        if huyen == None:
            tmp[1] = 1
        else:
            dem = 2
            check = True
            for i in huyen_formated:
                if i in huyen:
                    tmp[dem] = 1
                    print(i)
                    check = False
                    break
                else:
                    dem += 1
            if check == True:
                tmp[0] = 1
        vecs_district[cnt] = tmp
        cnt += 1
    print(vecs_district)
    print(vecs_district.shape)

    #_______________________________________________#
    vecs = np.concatenate((vecs, vecs_district), axis=1)
    print(vecs.shape)
    #_______________________________________________#

    # Job
    pre_mapping_dict = [[['cong nhan', 'cn', 'cnhan', 'lao dong', 'c.nhan', 'coong nhaon', 'may', 'cao su', 'cong', 'bao ve', 'nhan', 'sua chua'], 'cong nhan'
                    ],[['nhan vien', 'nv', 'thiet bi', 'trung cap', 'quan li', 'nhon vion', 'vien', 'tiep thi'], 'nhan vien'
                    ],[['giam dinh', 'giam sat', 'kiem tra', 'kt', 'quan doc', 'kiem soat', 'thanh tra'], 'nhan vien kiem tra'
                    ],[['ky thuat', 'kt', 'tro li', 'thu ky', 'quan ly', 'ky su', 'chuyen vien', 'tro ly', 'dien vien', 'quan doc', 'thu kho', 'tiep vien'], 'rich nhan vien'
                    ],[['lai', 'tai xe'], 'lai xe'
                    ],[['chien', 've'], 'army'
                    ],[['giao vien', 'giang vien', 'gv', 'giáo vien', 'dao tao'], 'giao vien'
                    ],[['ban hang', 'sale', 'market', 'kinh doanh', 'bhang', 'giao dich', 'tiep thi'], 'sale'
                    ],[['ke toan'], 'ke toan'
                    ],[['thu no'], 'bad guy'
                    ],[['cu nhan', 'cu nhn'], 'cu nhan'
                    ],[['xay dung', 'xd', 'son', 'tho', 'phu'], 'cong nhan part 2'
                    ],[['chu tich', 'bi thu', 'truong', 'can bo', 'cb', 'can', 'vien chuc'], 'can bo'
                    ],[['dieu duong', 'y te', 'y sy', 'duoc', 'bac sy', 'y si', 'cap duong', 'ho sinh', 'y', 'bac si'], 'y te'
                    ],[['giam doc', 'pho', 'dien vien', 'gdoc'], 'xin xo`'
                    ],[['giao hang'], 'shipper'
                    ]]
    jobs_dict = {}
    for i in pre_mapping_dict:
        for val in i[0]:
            jobs_dict[val] = i[1]
    print(jobs_dict)
    print(len(pre_mapping_dict))

    #------------------------------------------------------#

    # Job 
    # col from 0 to 17
    # col 0 means not found
    # col 1 means null
    vecs_jobs = np.ndarray(shape=(len(dists), 18), dtype=int)
    df = pd.read_csv(path + strPath, low_memory=False)
    jobs = []
    job = df['maCv'].values.tolist()
    for j in job:
        jobs.append(address.remove_accents(j))
    print(list(set(jobs_dict.values())))

    #-----------------------------------------------------------#

    cnt = 0
    for job in jobs:
        ar = np.zeros(18)
        tmp = set()
        if type(job) is str:
            for i in jobs_dict.keys():
                if i in job:
                    tmp.add(jobs_dict[i])
        else:
            ar[1] = 1  
        dem = 2
        if len(tmp) == 0:
            if ar[1] == 0:
                ar[0] = 1
        else:
            for i in list(set(jobs_dict.values())):
                if i in tmp:
                    ar[dem] = 1
                dem += 1
        vecs_jobs[cnt] = ar
        cnt += 1
    print(vecs_jobs)
    #-----------------------------------------------------------#
    vecs = np.concatenate((vecs, vecs_jobs), axis=1)
    #___________________________________________________________#
    # age
    # age 0 to 100
    # age 0 mean Null
    age_1 = df['age_source1'].values.tolist()
    age_2 = df['age_source2'].values.tolist()
    vecs_age = np.ndarray(shape=(len(dists), 100), dtype=int)

    #-----------------------------------------------------------#
    cnt = 0
    for i in range(len(age_1)):
        tmp = np.zeros(100)
    #     print(type(age_1[i]))
        if not math.isnan(age_1[i]):
            tmp[int(age_1[i])] = 1
        else:
            tmp[0] = 1
        if not math.isnan(age_2[i]):
            tmp[int(age_2[i])] = 1
        else:
            tmp[0] = 1
        vecs_age[cnt] = tmp
        cnt += 1
    #-----------------------------------------------------------#
    vecs = np.concatenate((vecs, vecs_jobs), axis=1)
    print(vecs.shape)
    #___________________________________________________________#

    f7 = pd.read_csv(path + './Data/field_7.csv', low_memory=False)
    f7 = f7['FIELD_7'].values.tolist()
    print(f7)
    print(len(f7))

    # Field 7
    # From 0 to 44
    # Value 0 mean null

    vecs_f7 = np.ndarray(shape=(len(dists), 45), dtype=int)
    f7_data = df['FIELD_7'].values.tolist()

    cnt = 0
    for i in f7_data:
        tmp = np.zeros(45)
        lst = string2list(i)
        
        if len(lst) == 0:
            tmp[0] = 1
        else:
            for j in lst:
                index = f7.index(j) + 1
                tmp[index] += 1
        vecs_f7[cnt] = tmp
        cnt += 1
    #____________________________________________________#
    vecs = np.concatenate((vecs, vecs_jobs), axis=1)
    print(vecs.shape)
    #____________________________________________________#

    return vecs

if __name__ == "__main__":
    
    encode('./Data/train.csv')