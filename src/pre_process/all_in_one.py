import os
import numpy as np
import pandas as pd

description = {'cat_features': {'count':[#'maCv',  # count encoding
#                                 'district',
                                'FIELD_9',
                                'FIELD_12',
                                'FIELD_13'],
                                'one_hot':[
#                                 'province',  # one hot encoding
                                'FIELD_17',
                                'FIELD_24',
                                'FIELD_35',
#                                 'FIELD_39',  #country code
                                'FIELD_40',
                                'FIELD_41',
                                'FIELD_43'
                               ]},
               'bool_features': ['FIELD_1',
                                 'FIELD_2',
                                 'FIELD_8',
                                 'FIELD_10',
                                 'FIELD_14',
                                 'FIELD_15',
                                 'FIELD_18',
                                 'FIELD_19',
                                 'FIELD_20',
                                 'FIELD_23',
                                 'FIELD_25',
                                 'FIELD_26',
                                 'FIELD_27',
                                 'FIELD_28',
                                 'FIELD_29',
                                 'FIELD_30',
                                 'FIELD_31',
                                 'FIELD_32',
                                 'FIELD_33',
                                 'FIELD_34',
                                 'FIELD_36',
                                 'FIELD_37',
                                 'FIELD_38',
                                 'FIELD_42',
                                 'FIELD_44',
                                 'FIELD_46',
                                 'FIELD_47',
                                 'FIELD_48',
                                 'FIELD_49',
                                ],
               'numerical_features': {'small':[#'age_source1',  # small, onehot-able
#                                     'age_source2',
                                    'FIELD_4',
                                    'FIELD_5',
                                    'FIELD_6',
                                    'FIELD_11',
                                    'FIELD_16',
                                    'FIELD_21',
                                    'FIELD_45',
                                    'FIELD_50',
                                    'FIELD_54'],
                                      'big':
                                    ['FIELD_3',      # big
                                    'FIELD_22',
                                    'FIELD_51',
                                    'FIELD_52',
                                    'FIELD_53',
                                    'FIELD_55',
                                    'FIELD_56',
                                    'FIELD_57']
               },
               'unknown': [#'FIELD_7',
                          ]
              }


def normalize(train_data: pd.DataFrame, description):
    train_data.fillna(-999.0, inplace=True)

    #     train_data['province'].replace(to_replace='Tỉnh Vĩnh phúc', value='Tỉnh Vĩnh Phúc', inplace=True)

    #     for i in range(train_data.shape[0]):
    #         if train_data['age_source1'][i] == np.nan and train_data['age_source2'][i] != np.nan:
    #             train_data.loc[3, i] = train_data['age_source2'][i]
    #         elif train_data['age_source2'][i] == np.nan and train_data['age_source1'][i] != np.nan:
    #             train_data.loc[4, i] = train_data['age_source1'][i]

    train_data['FIELD_9'].replace(to_replace='na', value=-1.0, inplace=True)
    train_data.replace(to_replace='None', value=-1.0, inplace=True)

    train_data['FIELD_40'].replace(to_replace=['08 02', '05 08 11 02'], value=-1.0, inplace=True)
    train_data['FIELD_43'].replace(to_replace='0', value=-1.0, inplace=True)

    for feature in description['bool_features']:
        train_data[feature].replace(to_replace=['FALSE',
                                                'Zezo',
                                                'Two',
                                                'GH',
                                                'FEMALE'], value=0, inplace=True)
        train_data[feature].replace(to_replace=['TRUE',
                                                'One',
                                                'T1',
                                                'MALE'], value=1, inplace=True)
#         train_data[feature].replace(to_replace='Missing', value=-999, inplace=True


def onehot_encode(ds: pd.Series, val_dict):
    res = np.zeros(shape=(ds.shape[0], len(val_dict)))
    for i in range(ds.shape[0]):
        if ds[i] in val_dict:
            res[i, val_dict[ds[i]]] = 1
    return res


def boolean_feature_encode(df: pd.DataFrame, bool_features):
    bool_feature_val = dict({0: 0, 1: 1, -999.0: 2, -1: 3})
    res = []
    for feature in bool_features:
        res.append(onehot_encode(df[feature], bool_feature_val))
    res = np.concatenate(res, axis=1)
    return res


def process(df: pd.DataFrame, all_data: pd.DataFrame, description):
    # one hot first
    dict_ = {float(i): i + 2 for i in range(6)}
    dict_[-1.0] = 0
    dict_[-999.0] = 1
    f21 = onehot_encode(df['FIELD_21'], dict_)
    f45 = onehot_encode(df['FIELD_45'], dict_)
    dict_.update({float(i): i + 2 for i in range(6, 11)})
    f6 = onehot_encode(df['FIELD_6'], dict_)
    f16 = onehot_encode(df['FIELD_16'], dict_)
    dict_.update({float(i): i + 2 for i in range(11, 16)})
    f4 = onehot_encode(df['FIELD_4'], dict_)
    f5 = onehot_encode(df['FIELD_5'], dict_)
    dict_.update({float(i): i + 2 for i in range(16, 101)})
    f11 = onehot_encode(df['FIELD_11'], dict_)
    f50 = onehot_encode(df['FIELD_50'], {i: j for j, i in enumerate(all_data['FIELD_50'].unique())})
    f54 = onehot_encode(df['FIELD_54'], {i: j for j, i in enumerate(all_data['FIELD_54'].unique())})

    f1 = [f4, f5, f6, f11, f16, f21, f45, f50, f54]
    f = []

    for type_ in description['cat_features']:
        for feature in description['cat_features'][type_]:
            dict_ = {i: j for j, i in enumerate(all_data[feature].unique())}
            fx = onehot_encode(df[feature], dict_)
            f.append(fx)

    f.extend(f1)

    # big numerical second
    f2 = [np.reshape(np.array([df[feature].values]), (df.shape[0], -1)) for feature in
          description['numerical_features']['big']]
    f.extend(f2)

    # age feature last
    f3 = np.zeros(shape=(df.shape[0], 4))  # add mean and is_different
    for i in range(df.shape[0]):
        f3[i, 0] = df['age_source1'][i]
        f3[i, 1] = df['age_source2'][i]
        f3[i, 2] = (f3[i, 0] + f3[i, 1]) / 2
        f3[i, 3] = 0
        if f3[i, 1] != f3[i, 0]:
            f3[i, 3] = 1
    #     f.extend(f3)
    # print([a.shape for a in f])

    # concatenate, boolean feature first
    res = np.concatenate([boolean_feature_encode(df, description['bool_features']), np.concatenate(f, axis=1), f3],
                         axis=1)
    return res


def main():
    train = pd.read_csv('./Data/train.csv', delimiter=',', low_memory=False)
    test = pd.read_csv('./Data/test.csv', delimiter=',', low_memory=False)
    del train['label']
    all_data = pd.concat([train, test])

    normalize(train, description)
    normalize(all_data, description)

    return process(train, all_data, description)


# print(main().shape)