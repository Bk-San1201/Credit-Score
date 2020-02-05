import pandas as pd
import os
from pandas import DataFrame
import csv
import json
import numpy as np
import address
import math


def new_columns():
    df = pd.read_csv('Data/train_input.csv', low_memory=False)
    ar = []
    job = df['maCv'].values.tolist()
    for j in job:
        ar.append(address.remove_accents(j))
    df['job'] = np.array(ar)
    df.to_csv('Data/train_input.csv', index=False)


def check_job():
    df = pd.read_csv('Data/train_input.csv', low_memory=False)
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
    pre_mapping_dict = [[['cong nhan', 'cn', 'cnhan', 'lao dong', 'c.nhan', 'coong nhaon', 'may'], 'cong nhan'
                ],[['nhan vien', 'nv'], 'nhan vien'
                ],[['ky thuat', 'kt', 'tro li', 'thu ky'], 'rich nhan vien'
                ],[['lai'], 'lai xe'
                ],[['chien'], 'army'
                ],[['giao vien', 'giang vien'], 'giao vien'
                ],[['ban hang', 'sale', 'market', 'kinh doanh', 'bhang'], 'sale'
                ],[['ke toan'], 'ke toan'
                ],[['thu no'], 'bad guy'
                ],[['cu nhan', 'cu nhn'], 'cu nhan'
                ],[['xay dung', 'xd', 'son', 'tho', 'phu'], 'cong nhan part 2'
                ],[['chu tich', 'bi thu', 'truong'], 'can bo'
                ]]
    jobs_dict = {}
    for i in pre_mapping_dict:
        for val in i[0]:
            jobs_dict[val] = i[1]
    # print(jobs_dict)
    lstJob = ['cong nhan', 'cn', 'cnhan', 'lao dong',
              'c.nhan', 'coong nhaon', 'may', 'nhan vien', 'nv',
              'ky thuat', 'kt', 'tro li', 'thu ky', 'lai', 'chien',
              'giao vien', 'giang vien', 'ban hang', 'sale', 'market',
              'kinh doanh', 'bhang', 'ke toan', 'cu nhan', 'cu nhn',
              'cu nhan', 'cu nhn', 'xay dung', 'xd', 'son', 'tho', 'phu',
              'chu tich', 'bi thu', 'truong']
    df = pd.read_csv('Data/train_input.csv', low_memory=False)
    jobs = df['job'].values.tolist()
    jobs_converted = []

    # for job in jobs:
    #     if type(job) is str:
    #         for i in lstJob:
    #             if i in job:
    #                 break
    #         else:
    #             print(job)


# if __name__ == "__main__":
#     os.chdir(os.path.dirname(os.path.dirname(__file__))[:-4])
#     convert_job()
