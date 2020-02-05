import pandas as pd
import numpy as np
import os

ONE_HOT_THRESHOLD = 300
COUNT_ENCODING_THRESHOLD = 4000


def get_features_info():
    f = open('Data/train.csv', encoding="UTF8")
    label = f.readline().split(',')
    f.close()

    inp = pd.read_csv('Data/train.csv', delimiter=',', low_memory=False)
    inp = inp.to_numpy(dtype=str)
    shape = inp.shape
    train_info = [dict() for _ in range(shape[1])]
    for sample in inp:
        for i in range(shape[1]):
            train_info[i][sample[i]] = None

    inp1 = pd.read_csv('Data/test.csv', delimiter=',', low_memory=False)
    inp1 = inp1.to_numpy(dtype=str)
    shape = inp1.shape
    inp1 = np.insert(inp1, 1, [str(0) for _ in range(shape[0])], 1)
    inp = np.append(inp, inp1, axis=0)
    all_info = [dict() for _ in range(shape[1] + 1)]
    for sample in inp:
        for i in range(shape[1]):
            all_info[i][sample[i]] = None
    return label, train_info, all_info, inp


def write_to_file(label, train_info, all_info):
    f = open('info.csv', 'w')
    ','.join(map(str, label))
    f.write(label)
    f.write("\n")

    train_info = [str(len(column)) for column in train_info]
    train_info = ",".join(train_info)
    f.write(train_info)
    f.write("\n")

    all_info = [str(len(column)) for column in all_info]
    all_info = ",".join(all_info)
    f.write(all_info)
    f.close()


def normalize(train: pd.DataFrame):
    train.fillna("Missing", inplace=True)

    train['province'].replace(to_replace='Tỉnh Vĩnh phúc', value='Tỉnh Vĩnh Phúc', inplace=True)

    for i in range(train.shape[0]):
        if train['age_source1'][i] == np.nan and train['age_source2'][i] != np.nan:
            train.loc[3, i] = train['age_source2'][i]
        elif train['age_source2'][i] == np.nan and train['age_source1'][i] != np.nan:
            train.loc[4, i] = train['age_source1'][i]

    train['FIELD_9'].replace(to_replace='na', value=-1, inplace=True)
    train.replace(to_replace='None', value=-1, inplace=True)

    train['FIELD_40'].replace(to_replace=['08 02', '05 08 11 02'], value=-1, inplace=True)
    train['FIELD_43'].replace(to_replace='0', value=-1, inplace=True)


if __name__ == '__main__':
    if os.path.dirname(os.path.dirname(__file__))[-3:] == 'src':
        os.chdir(os.path.dirname(os.path.dirname(__file__))[:-4])


