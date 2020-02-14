import sys, os
import numpy as np
import pandas as pd

import src.Pre_process.field_to_vec as first
import src.Pre_process.all_in_one as sec

train1, test1 = first.main()
train2, test2 = sec.main()
X_train = np.concatenate([train1, train2], axis=1)
X_test= np.concatenate([test1, test2], axis=1)
print(X_train.shape, X_test.shape)

from sklearn.svm import SVC
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, pd.read_csv('../.././Data/train.csv')['label'])

# y_pred = svclassifier.predict(X_test)
# print(y_pred)