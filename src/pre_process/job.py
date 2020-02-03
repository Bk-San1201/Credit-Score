import pandas as pd
from pandas import DataFrame
import csv
import json
import numpy as np
import address
import math


def new_columns():
    df = pd.read_csv('./Data/train_input.csv', low_memory=False)
    ar = []
    job = df['maCv'].values.tolist()
    for j in job:
        ar.append(address.remove_accents(j))
    df['job'] = np.array(ar)
    df.to_csv('./Data/train_input.csv', index=False)


def check_job():
    df = pd.read_csv('./Data/train_input.csv', low_memory=False)
    jobs = df['job'].values.tolist()
    setJob = set()
    for job in jobs:
        try:
            tmp = job.split()[:2]
            s = tmp[0] + ' ' + tmp[1]
            setJob.add(s)
        except:
            continue
    for s in setJob:
        print(s)


def convert_job():
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
                ],[['none', 'undefined'], 'none'
                ],[['dieu duong', 'y te', 'y sy', 'duoc', 'bac sy', 'y si', 'cap duong', 'ho sinh', 'y', 'bac si'], 'y te'
                ],[['giam doc', 'pho', 'dien vien', 'gdoc'], 'xin xo`'
                ],[['giao hang'], 'shipper'
                ]]
    jobs_dict = {}
    for i in pre_mapping_dict:
        for val in i[0]:
            jobs_dict[val] = i[1]
    print(jobs_dict)
    
    df = pd.read_csv('./Data/train_input.csv', low_memory=False)
    jobs = df['job'].values.tolist()
    # jobs_converted = []

    f = open("./Data/test.txt", 'w', encoding='utf8')

    for job in jobs:
        if type(job) is str:
            for i in jobs_dict.keys():
                if i in job:
                    # f.write(jobs_dict[i] + '-')
                    break
            else:
                f.writelines(job)
                f.write('\n')
            # f.write('\n')
        # else:
            # f.write('Null\n')
    f.close()

if __name__ == "__main__":
    convert_job()
