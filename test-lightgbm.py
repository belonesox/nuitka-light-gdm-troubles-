# coding: utf-8
from pathlib import Path

# import pandas as pd
# from sklearn.metrics import mean_squared_error

import lightgbm as lgb

print('Loading data...')
# load or create your dataset
regression_example_dir = Path(__file__).parent.absolute()

# df_train1 = pd.read_csv(str(regression_example_dir / 'regression.train'), header=None, sep='\t')
# df_test1 = pd.read_csv(str(regression_example_dir / 'regression.test'), header=None, sep='\t')

import numpy as np
df_train2 = np.loadtxt(str(regression_example_dir / 'regression.train'), delimiter="\t")#, skiprows=1)
df_test2 = np.loadtxt(str(regression_example_dir / 'regression.train'), delimiter="\t")#, skiprows=1)
 
# y_train1 = df_train1[0]
# y_test1 = df_test1[0]
y_train2 = df_train2[:,0]
y_test2 = df_test2[:,0]

# create dataset for lightgbm
# labels = [f"{i}" for i in range(X_train.shape[1])]

# X_train1 = df_train1.drop(0, axis=1)
# X_test1 = df_test1.drop(0, axis=1)

X_train2 = df_train2[:,1:]
X_test2 = df_test2[:,1:]

# lgb_train1 = lgb.Dataset(X_train1, y_train1) #, label=labels)

lgb_train2 = lgb.Dataset(X_train2, y_train2) #, label=labels)



lgb_eval2 = lgb.Dataset(X_test2, y_test2, reference=lgb_train2)

# specify your configurations as a dict
params = {
    'boosting_type': 'gbdt',
    'objective': 'regression',
    'metric': {'l2', 'l1'},
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'verbose': 0
}

print('Starting training...')
# train
gbm = lgb.train(params,
                lgb_train2,
                num_boost_round=20,
                valid_sets=lgb_eval2,
                callbacks=[lgb.early_stopping(stopping_rounds=5)])

print('Saving model...')
# save model to file
gbm.save_model('model.txt')

print('Starting predicting...')
# predict
y_pred2 = gbm.predict(X_test2, num_iteration=gbm.best_iteration)
print(y_pred2)
# eval
# rmse_test = mean_squared_error(y_test2, y_pred2) ** 0.5
# print(f'The RMSE of prediction is: {rmse_test}')
